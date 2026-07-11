# Run Records

Add one valid JSON file per run named `run-NNN.json`.

```json
{
  "run": 1,
  "date": "YYYY-MM-DD",
  "phase": "explore",
  "objective": "One sentence",
  "actions": ["Concrete action"],
  "filesChanged": ["path"],
  "evidenceAdded": ["EVIDENCE-001"],
  "hypothesis": "What this run tested",
  "result": "supported|contradicted|inconclusive",
  "checks": ["Command or verification"],
  "limitations": ["Known limitation"],
  "next": "Smallest justified next action"
}
```
