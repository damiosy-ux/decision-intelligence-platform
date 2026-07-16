# Sample Output

```text
accepted=23 harvested=23 results=1

Fixture                                  Side Entity             Score Class FailedRules
-------                                  ---- ------             ----- ----- -----------
Example Home vs Example Away             Away Example Away       1     lean  loss_suppression
```

The output is intentionally compact:

- `accepted`: source fixtures that passed competition/source filtering
- `harvested`: accepted fixtures with usable statistics tables
- `results`: retained decisions after offline evaluation
- `FailedRules`: rule groups that did not pass for the retained result
