# Directed Unknown Machine 2

An autonomous software experiment that begins without a product idea, explores real problems, and converges on one useful, testable artifact.

V2 is deliberately domain-neutral. It rewards demonstrated usefulness rather than novelty alone.

## Start here

The agent must read [00_START_HERE.md](00_START_HERE.md) before every run. It defines instruction precedence and the run protocol.

Core files:

- `MISSION.md` — desired outcome
- `SEED.md` — deliberately minimal starting prompt
- `AGENT_RULES.md` — research, building, evidence, and safety rules
- `JUDGING.md` — evaluation criteria
- `AGENT_STATE.md` — current phase and objective
- `OPPORTUNITIES.md` — candidate problems and falsification evidence
- `EVIDENCE.md` — source and claim ledger
- `DECISIONS.md` — selection, rejection, and pivot decisions
- `CHANGELOG.md` — human-readable progress
- `THIRD_PARTY_NOTICES.md` — reused material and licenses
- `RUNS/` — machine-readable run records

## Selected prototype

The experiment selected a conservative secondhand recall screener. It accepts typed product-label fields, ranks candidates from the official CPSC recall feed, and always preserves human review.

### Quick start

Python 3.10 or newer is sufficient; there are no third-party dependencies.

```bash
python recall_screen.py --brand Insignia --model NS-RGFGSS1 --product "gas range"
```

The first run downloads the public recall feed to `.cache/cpsc_recalls.json`. Use `--refresh` to update it or `--data path/to/recalls.json` for a controlled input file.

Run the tests:

```bash
python -m unittest -v tests/test_recall_screen.py
```

Possible outcomes are `MATCHED RECALL — HOLD`, `POSSIBLE MATCH — HOLD`, `INSUFFICIENT IDENTITY`, and `NO CANDIDATE FOUND — NOT A CLEARANCE`.

This tool does not provide legal or safety clearance. A missing candidate never means that a product is safe or has not been recalled.
