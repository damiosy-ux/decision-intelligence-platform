# Sample Output

```text
accepted=23 harvested=23 results=1

Fixture                      Side Entity         Score Class PassedRules     FailedRules
-------                      ---- ------         ----- ----- -----------     -----------
Example Alpha vs Example Beta Home Example Alpha 2     high  signal_a,signal_b -
```

The output is intentionally compact:

- `accepted`: source fixtures that passed competition/source filtering
- `harvested`: accepted fixtures with usable statistics tables
- `results`: retained decisions after offline evaluation
- `PassedRules`: rule groups that passed for the retained result
- `FailedRules`: rule groups that did not pass for the retained result

Scores and labels in this synthetic example are deterministic rule outcomes. They are not statistical probability claims.
