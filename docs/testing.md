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
- rule-based result retention
- classification output
- failed-rule output

## Next Test Areas

- tie-breaking behavior
- invalid record handling
- config validation
- output serialization
