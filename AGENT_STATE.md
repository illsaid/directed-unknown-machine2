# Agent State

## Agent

Scheduled autonomous repository agent.

## Current phase

Build — first complete loop.

## Run count

5

## Selected direction

Secondhand recall screener.

## Current understanding

The repository now contains a dependency-free command-line intake tool that downloads or reads CPSC recall JSON, accepts typed brand/model/UPC/product fields, deterministically ranks candidates, exposes match reasons, and returns conservative outcomes with official evidence links.

Seven tests cover exact model, partial model, ambiguous partial model, exact UPC, insufficient identity, no candidate without clearance, and null fields from official records. The first live corpus run exposed the null-field defect; after the fix, an Insignia model case returned the correct official recall with hazard, remedy, reasons, and a hold action.

This is technical validation only. General retrieval accuracy, false-negative behavior, review-time improvement, and real-user usefulness remain unmeasured.

## Current objective

Create a reproducible held-out evaluation set from real recall records without leaking target text into queries, compare candidate retrieval and review time with manual CPSC search, and document failure modes.

## Constraints

- Read `00_START_HERE.md` before every run.
- Do not use the user's other projects or private context for direction.
- Never treat no candidate as clearance.
- Require human confirmation before a final item-identity decision.
- Prefer deterministic matching and expose why each candidate ranked.
- No external actions or transactions without explicit human approval.

## Last action

Run 5: implemented the minimal intake CLI, added seven safety and regression tests, fixed live-corpus null handling, and verified one authoritative end-to-end case.

## Next suggested action

Run 6 should evaluate representative and adverse held-out cases, measure retrieval and review effort against manual search, and fix the most consequential demonstrated failure.
