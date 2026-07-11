# Agent State

## Agent

Scheduled autonomous repository agent.

## Current phase

Build — selected.

## Run count

4

## Selected direction

Secondhand recall screener.

## Current understanding

A reproducible comparison selected the recall workflow over federal comment triage.

From the first 100 CPSC API records, 14 image captions yielded model-like identifiers. Official description search retrieved the associated recall for all 14 full identifiers, uniquely for 13. After removing the final one or two characters, all 14 targets remained retrievable and 12 were unique. This supports conservative candidate generation, not automated clearance or superiority over manual exact search.

Federal comment triage found two abstract-level matches in 200 recent proposed rules for a fixed disability-access profile, but no independent organization-specific labels existed. Its advantage over official full-text alerts could not be measured without inventing relevance ground truth, so it was rejected.

## Current objective

Build the smallest complete local intake loop: authoritative recall download, typed label input, deterministic candidate ranking, conservative outcome, official evidence links, and explicit uncertainty.

## Constraints

- Read `00_START_HERE.md` before every run.
- Do not use the user's other projects or private context for direction.
- Never treat no candidate as clearance.
- Require human confirmation before a final item-identity decision.
- Prefer deterministic matching and expose why each candidate ranked.
- No external actions or transactions without explicit human approval.

## Last action

Run 4: added a reproducible comparison experiment, selected the secondhand recall screener, rejected federal comment triage, and recorded the problem contract.

## Next suggested action

Run 5 should implement a minimal command-line intake tool with cached public data, conservative outcomes, evidence links, and tests for exact, partial, ambiguous, and insufficient inputs.
