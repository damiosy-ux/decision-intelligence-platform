# Testing

The Python package includes small unit tests for normalization and evaluation behavior.

Run locally:

```powershell
$env:PYTHONPATH = "src"
python -m pytest
```

The GitHub Actions workflow runs the same test suite on every push and pull request.

## Current Test Coverage

- raw sample row normalization
- incomplete-evidence rejection
- invalid metric rejection
- rule-based result retention
- classification output
- failed-rule output

## Next Test Areas

- tie-breaking behavior
- config validation
- output serialization
