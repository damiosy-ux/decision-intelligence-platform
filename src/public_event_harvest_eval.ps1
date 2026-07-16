$ErrorActionPreference = "SilentlyContinue"

$Headers = @{ "User-Agent" = "Mozilla/5.0" }
$FeedUrl = "https://live10.goaloo28.com/gf/data/bf_us1.js"
$EventPageTemplate = "https://live10.goaloo28.com/football/x/live-{0}"

function ConvertFrom-HtmlText([string]$Value) {
  return (($Value -replace "<[^>]+>", "") -replace "&nbsp;", " ").Trim()
}

function Split-JavaScriptArray([string]$Value) {
  $items = New-Object System.Collections.Generic.List[string]
  $current = ""
  $inQuote = $false

  for ($i = 0; $i -lt $Value.Length; $i++) {
    $char = $Value[$i]
    if ($char -eq "'" -and ($i -eq 0 -or $Value[$i - 1] -ne "\")) {
      $inQuote = -not $inQuote
    }

    if ($char -eq "," -and !$inQuote) {
      $items.Add($current.Trim())
      $current = ""
      continue
    }

    $current += $char
  }

  $items.Add($current.Trim())
  return @($items)
}

function ConvertFrom-JsString([string]$Value) {
  $Value = $Value.Trim()
  if ($Value.StartsWith("'") -and $Value.EndsWith("'")) {
    $Value = $Value.Substring(1, $Value.Length - 2)
  }

  return ConvertFrom-HtmlText ($Value -replace "\\'", "'")
}

function Test-RegularSeasonCompetition($Competition) {
  $text = (($Competition.ShortName + " " + $Competition.Name + " " + $Competition.SourceRoute + " " + $Competition.Phase) -replace "\\'", "'")
  $rejectPattern = "(?i)\b(cup|friendly|shield|super cup|playoff|play-off|promotion|relegation|qualif|qualification|knockout|champions league|europa league|conference league|libertadores|sudamericana|afc cup|concacaf|exhibition)\b"

  if ($text -match $rejectPattern) { return $false }
  if ($Competition.SourceRoute -notmatch "(?i)(League|SubLeague)\.aspx") { return $false }

  return $true
}

function Get-FeedFixtures([string]$Url) {
  $feed = (Invoke-WebRequest -Uri $Url -UseBasicParsing -Headers $Headers).Content
  $competitions = @{}

  foreach ($match in [regex]::Matches($feed, "B\[(\d+)\]=\[([^\r\n]+?)\];")) {
    $parts = Split-JavaScriptArray $match.Groups[2].Value
    $competitions[[int]$match.Groups[1].Value] = [pscustomobject]@{
      ShortName = ConvertFrom-JsString $parts[1]
      Name = ConvertFrom-JsString $parts[2]
      SourceRoute = ConvertFrom-JsString $parts[5]
      Phase = if ($parts.Count -gt 7) { ConvertFrom-JsString $parts[7] } else { "" }
    }
  }

  $fixtures = @()
  foreach ($match in [regex]::Matches($feed, "A\[(\d+)\]=\[([^\r\n]+?)\];")) {
    $parts = Split-JavaScriptArray $match.Groups[2].Value
    $competitionIndex = [int]$match.Groups[1].Value
    $competition = $competitions[$competitionIndex]

    if (!$competition -or !(Test-RegularSeasonCompetition $competition)) { continue }

    $fixtures += [pscustomobject]@{
      EventId = [int]$parts[0]
      HomeEntity = ConvertFrom-JsString $parts[4]
      AwayEntity = ConvertFrom-JsString $parts[5]
      Competition = $competition.Name
    }
  }

  return $fixtures
}

function Get-TableCells([string]$RowHtml) {
  @([regex]::Matches($RowHtml, "<t[dh][^>]*>([\s\S]*?)</t[dh]>") | ForEach-Object {
    ConvertFrom-HtmlText $_.Groups[1].Value
  })
}

function ConvertFrom-TeamStatisticsTable([string]$Html) {
  $sectionStart = $Html.IndexOf("Team Statistics")
  if ($sectionStart -lt 0) { return $null }

  $section = $Html.Substring($sectionStart, [math]::Min(6000, $Html.Length - $sectionStart))
  $table = [regex]::Match($section, "<table[^>]*team-table-other[^>]*>[\s\S]*?</table>").Value
  if (!$table) { return $null }

  $stats = @{
    Home = @{ L3 = @{}; L10 = @{} }
    Away = @{ L3 = @{}; L10 = @{} }
  }

  foreach ($row in [regex]::Matches($table, "<tr[^>]*>[\s\S]*?</tr>")) {
    $cells = Get-TableCells $row.Value
    if ($cells.Count -lt 6) { continue }

    if ($cells[1] -eq "Goal") {
      $stats.Home.L3.GF = [double]$cells[0]
      $stats.Away.L3.GF = [double]$cells[2]
      $stats.Home.L10.GF = [double]$cells[3]
      $stats.Away.L10.GF = [double]$cells[5]
    }

    if ($cells[1] -eq "Loss") {
      $stats.Home.L3.GA = [double]$cells[0]
      $stats.Away.L3.GA = [double]$cells[2]
      $stats.Home.L10.GA = [double]$cells[3]
      $stats.Away.L10.GA = [double]$cells[5]
    }
  }

  if ($null -eq $stats.Home.L3.GF -or $null -eq $stats.Home.L3.GA) { return $null }
  return $stats
}

function Invoke-Harvest($Fixtures) {
  $records = @()

  foreach ($fixture in $Fixtures) {
    $eventUrl = $EventPageTemplate -f $fixture.EventId
    $html = (Invoke-WebRequest -Uri $eventUrl -UseBasicParsing -Headers $Headers -TimeoutSec 8).Content
    $stats = ConvertFrom-TeamStatisticsTable $html
    if (!$stats) { continue }

    $records += [pscustomobject]@{
      Fixture = "$($fixture.HomeEntity) vs $($fixture.AwayEntity)"
      Competition = $fixture.Competition
      HomeEntity = $fixture.HomeEntity
      AwayEntity = $fixture.AwayEntity
      Stats = $stats
    }
  }

  return $records
}

function Test-Selection($Record, [string]$Side, [string]$Entity, $Selected, $Opponent) {
  $growthSignal = (
    $Selected.L3.GF -ge 2.0 -and
    $Selected.L10.GF -ge 2.0 -and
    $Opponent.L3.GF -le 1.3 -and
    $Opponent.L10.GF -le 1.3
  )

  $lossSuppression = (
    $Selected.L3.GA -le 1.3 -and
    $Selected.L10.GA -le 1.3 -and
    $Opponent.L3.GA -ge 2.0 -and
    $Opponent.L10.GA -ge 2.0
  )

  $score = 0
  if ($growthSignal) { $score += 1 }
  if ($lossSuppression) { $score += 1 }
  if ($score -eq 0) { return $null }

  $failedRules = @()
  if (!$growthSignal) { [void]($failedRules += "growth_signal") }
  if (!$lossSuppression) { [void]($failedRules += "loss_suppression") }

  return [pscustomobject]@{
    Fixture = $Record.Fixture
    Side = $Side
    Entity = $Entity
    Score = $score
    Class = if ($score -eq 2) { "high_confidence" } else { "lean" }
    FailedRules = if ($failedRules.Count) { $failedRules -join "," } else { "-" }
    AlignmentDistance = [math]::Abs($Selected.L3.GF - 2.0) +
      [math]::Abs($Selected.L10.GF - 2.0) +
      [math]::Abs($Opponent.L3.GF - 1.3) +
      [math]::Abs($Opponent.L10.GF - 1.3) +
      [math]::Abs($Selected.L3.GA - 1.3) +
      [math]::Abs($Selected.L10.GA - 1.3) +
      [math]::Abs($Opponent.L3.GA - 2.0) +
      [math]::Abs($Opponent.L10.GA - 2.0)
  }
}

function Invoke-OfflineEvaluation($HarvestedRecords) {
  $results = @()

  foreach ($record in $HarvestedRecords) {
    $home = Test-Selection $record "Home" $record.HomeEntity $record.Stats.Home $record.Stats.Away
    $away = Test-Selection $record "Away" $record.AwayEntity $record.Stats.Away $record.Stats.Home

    if ($home -and !$away) { $results += $home; continue }
    if ($away -and !$home) { $results += $away; continue }

    if ($home -and $away) {
      if ($home.Score -gt $away.Score) { $results += $home; continue }
      if ($away.Score -gt $home.Score) { $results += $away; continue }

      $distanceGap = [math]::Abs($home.AlignmentDistance - $away.AlignmentDistance)
      if ($distanceGap -ge 1.0) {
        $results += @($home, $away | Sort-Object AlignmentDistance)[0]
      }
    }
  }

  return @($results | Where-Object { $_.Fixture -and $_.Score -ge 1 })
}

$fixtures = Get-FeedFixtures $FeedUrl
$harvest = Invoke-Harvest $fixtures
$results = Invoke-OfflineEvaluation $harvest

Write-Host "accepted=$($fixtures.Count) harvested=$($harvest.Count) results=$($results.Count)"
$results |
  Sort-Object @{ Expression = "Score"; Descending = $true }, Fixture |
  Select-Object Fixture, Side, Entity, Score, Class, FailedRules |
  Format-Table -AutoSize
