# Agent Rules

## Explore problems, not artifacts

Public datasets, repositories, APIs, archives, filings, records, and websites are research material. They are not automatically the product.

Promising patterns may include fragmented information, repetitive reconciliation, underserved small users, consequential data gaps, and recurring decisions. These are prompts, not required domains.

Do not choose a direction solely because its data is easy to obtain.

## Exploration

Before converging, investigate at least five candidate problems across at least three materially different domains.

For each candidate, record in `OPPORTUNITIES.md`:

- specific user;
- task or decision;
- current workaround;
- public evidence the problem exists;
- frequency and consequence;
- required inputs;
- actionable output;
- existing alternatives;
- reason a small project could compete;
- fastest useful experiment;
- strongest reason the idea may be wrong.

Research must try to disprove ideas, not merely justify them.

Converge no later than Run 6 unless `AGENT_STATE.md` records concrete evidence that exactly one additional exploration run is necessary.

## Selection

Score serious candidates from 1–5 on pain, frequency, user clarity, actionability, input access, weakness of alternatives, validation feasibility, buildability, and continuation value.

Record why the selected problem won and why the strongest alternatives lost.

Before substantial implementation, add a problem contract to `DECISIONS.md`:

> For [specific user], when [recurring situation], the project takes [available input] and produces [actionable output], improving [time, accuracy, cost, risk, or access] compared with [current workaround].

Also record the falsification condition, exclusions, smallest complete version, and validation method.

## Building

Build the smallest complete loop:

```text
real input -> useful transformation -> actionable output -> verification
```

Prefer real data over fixtures, one complete workflow over disconnected features, evidence links over unsupported summaries, deterministic processing where practical, explicit uncertainty, simple local operation, and an interface appropriate to the user.

Do not add AI merely to appear sophisticated.

## Run discipline

Every run must do at least one:

- gather evidence that changes a decision;
- test or falsify a hypothesis;
- produce or improve executable behavior;
- validate on real cases;
- fix a demonstrated defect;
- improve the target workflow.

Documentation alone does not count except during final packaging.

Each run should normally change no more than three working files. State, evidence, changelog, and run-record files do not count.

Every run updates `AGENT_STATE.md`, `CHANGELOG.md`, and one machine-readable file under `RUNS/`.

## Evidence

For every material factual claim, retain the source, retrieval date, relevant evidence, source type, confidence, and verification status.

Do not present missing data as absence, a proxy as fact, a sample as a population, correlation as causation, or pending status as final. Do not invent users, interviews, revenue, testimonials, or demand.

Use third-party material only when permitted and record copied or adapted material in `THIRD_PARTY_NOTICES.md`.

## Validation

Before final packaging:

- run the complete workflow end to end;
- test representative and adverse cases;
- compare with the current workaround or a real alternative;
- measure at least one relevant outcome;
- document failures;
- show that the result supports an action.

If no outside user participates, distinguish technical validation from user validation.

## Product consideration

A commercial product is optional. If proposing one, identify the user and buyer, recurring value, current alternative, reason to switch, distribution path, operating burden, legal and data dependencies, compounding value, and why an incumbent would not absorb it.

A large market is not evidence of a viable product.

## Pivoting

Pivot when evidence shows the problem is unimportant, inputs are unavailable, output is not actionable, existing tools solve it adequately, validation is infeasible, or the prototype has no credible user value. Record what failed and which assumption should not be repeated.

## Safety

Research is authorized. External transactions, outreach, account creation, bidding, purchases, legal filings, operational deployment, and publication outside this repository require explicit human approval.
