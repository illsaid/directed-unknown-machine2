# Decisions

## Bootstrap — V2 experiment design

The repository begins without a domain or product idea.

The experiment is constrained at the evaluation layer rather than the subject layer: it may explore broadly, but success requires a specific user, recurring job, actionable output, public evidence, and measured validation.

The agent may not inspect or derive direction from the user's other projects or private context. Independent overlap is allowed only when the public evidence trail is recorded.

No direction has been selected.


## Run 3 — Shortlist by public-record sufficiency

Shortlisted:

1. **Secondhand recall screener** — Consequence and item-level action are strong. Recent records always supplied hazard and remedy evidence, but only 29/50 supplied model-related text or a UPC. The viable scope is evidence-linked candidate review with an `INSUFFICIENT IDENTITY` outcome, not automated clearance.
2. **Federal comment-opportunity triage** — The public API supplied an abstract, close date, docket identifier, and comment route for 39/50 recent proposed rules. The viable scope is organization-specific relevance triage, not notification.

Rejected:

- **Provider-directory consistency auditor** — Public-source disagreement cannot establish whether a provider is actually available; useful validation requires authoritative roster or attestation data not available to this experiment.
- **Solicitation amendment brief** — SAM.gov already follows changes, historical versions require a separate data route, and an API key/account would be needed for the intended workflow.
- **Step-free transit disruption guard** — The official status page and ELstat already address outages, while the API requires registration and path-level topology remains unverified.

No final direction has been selected. Run 4 must compare the two shortlisted transformations against their incumbent workflows before convergence.


## Run 4 — Select the secondhand recall screener

**Selected:** Secondhand recall screener.

**Rejected finalist:** Federal comment-opportunity triage. It could surface abstract-level candidates, but this experiment has no independent organization-specific relevance labels and therefore cannot demonstrate improvement over free full-text alerts without inventing ground truth.

### Problem contract

> For an intake worker or listing operator at a small secondhand seller, when a product is being considered for inventory, the project takes available label text, brand, model, product type, and optional UPC and produces a conservative, evidence-linked recall candidate decision, designed to reduce repeated search work and missed candidate recalls compared with manually constructing CPSC searches for each item.

### Falsification condition

Stop or pivot if held-out partial-label cases fail to retrieve the correct candidate often enough for safe triage, if ambiguous queues are routinely unmanageable, or if the workflow does not reduce measured review time relative to manual CPSC search.

### Exclusions

- No legal or safety clearance.
- No claim that no search result means no recall.
- No automatic sale approval.
- No final product-identity determination without human confirmation.
- No outreach, marketplace action, or transaction.

### Smallest complete version

A local tool that downloads authoritative recall records, accepts typed label fields, ranks candidates, and returns one of:

- `MATCHED RECALL — HOLD`
- `POSSIBLE MATCH — HOLD`
- `INSUFFICIENT IDENTITY`
- `NO CANDIDATE FOUND — NOT A CLEARANCE`

Every candidate output must link to the official notice and show the fields that matched or remain unconfirmed.

### Validation method

Use held-out real recall records to create partial-label cases without exposing the target notice to the matcher. Compare correct-candidate retrieval, ambiguity, failure behavior, and review time with manual CPSC search. Distinguish technical validation from user validation.
