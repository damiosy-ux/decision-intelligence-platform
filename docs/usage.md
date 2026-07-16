# Usage

Run the current prototype from PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File .\src\public_event_harvest_eval.ps1
```

The script follows a two-phase workflow:

1. Harvest accepted source records.
2. Evaluate the harvested records offline.

The result includes:

- accepted source count
- harvested record count
- retained result count
- retained entities
- score
- class
- failed rule groups

Configuration is documented in `config/example-rules.json`. The current script still contains inline thresholds, but the roadmap moves these values into external rule files.
