# Start Here

This is the controlling entrypoint for every autonomous run.

## Instruction precedence

When instructions conflict:

1. Human instructions for the current run
2. `00_START_HERE.md`
3. `MISSION.md`
4. `AGENT_RULES.md`
5. `JUDGING.md`
6. `AGENT_STATE.md`
7. Other repository documents

Never treat generated state, an old decision, or the current prototype as more authoritative than the mission and rules.

## Read before acting

Read completely:

- `MISSION.md`
- `SEED.md`
- `AGENT_RULES.md`
- `JUDGING.md`
- `AGENT_STATE.md`
- `OPPORTUNITIES.md`
- `DECISIONS.md`
- `EVIDENCE.md`
- `THIRD_PARTY_NOTICES.md`

Inspect the working tree and latest run record.

## Run protocol

1. Establish the current phase and objective.
2. Choose the smallest action that can change a decision, falsify a hypothesis, improve executable behavior, or validate usefulness.
3. Perform the work.
4. Run proportionate checks.
5. Record evidence and uncertainty.
6. Update `AGENT_STATE.md`, `CHANGELOG.md`, and one record under `RUNS/`.
7. Update `DECISIONS.md` only for an actual selection, rejection, or pivot.
8. Stop after one coherent increment.

## Hard constraints

- Do not inspect sibling repositories, unrelated local files, private user context, conversation memory, or connected private services to obtain a project idea.
- Direction must arise from public research recorded in this repository.
- Do not contact, message, enroll, solicit, purchase from, bid on, or transact with outsiders without explicit human approval.
- Do not perform legal, financial, medical, regulatory, or physical-world actions.
- Do not claim demand, adoption, savings, accuracy, or validation that was not measured.
- Do not present a proxy as the underlying fact.
- Do not use missing data as proof that something did not occur.
- Do not optimize for an impressive report at the expense of a useful artifact.

## Current status

Run 0. Exploration has not begun. No direction has been selected.
