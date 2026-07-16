# Contributing

This project is currently maintained as a focused portfolio and research prototype.

Contributions should stay within the public scope of the repository:

- use synthetic or clearly public sample data
- avoid credentials, private feeds, or proprietary datasets
- keep rules generic and explainable
- add tests for evaluation behavior
- document assumptions and limitations

## Local Checks

```powershell
$env:PYTHONPATH = "src"
python -m pytest
```

## Pull Request Expectations

- Describe the problem being solved.
- Explain any new rule or model behavior.
- Include tests for evaluator changes.
- Do not include private data or operational details.
