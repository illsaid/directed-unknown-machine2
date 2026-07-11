# Opportunities

Record candidate problems, not product pitches. Do not remove rejected candidates.

## Candidate template

### Candidate: [short name]

- **Domain:**
- **Specific user:**
- **Recurring job or decision:**
- **Current workaround:**
- **Evidence of friction:**
- **Frequency:**
- **Consequence:**
- **Required inputs:**
- **Actionable output:**
- **Existing alternatives:**
- **Why a small project might compete:**
- **Fastest useful experiment:**
- **Strongest falsification argument:**
- **Evidence references:** EVIDENCE-[IDs]
- **Status:** exploring | shortlisted | selected | rejected

| Criterion | 1–5 |
|---|---:|
| Pain | |
| Frequency | |
| User clarity | |
| Actionability | |
| Input access | |
| Existing-alternative gap | |
| Validation feasibility | |
| Buildability | |
| Continuation value | |

**Total:** /45

## Candidates

### Candidate: Secondhand recall screener

- **Domain:** Consumer-product safety / resale operations
- **Specific user:** Intake worker or listing operator at a small thrift, consignment, liquidation, or online-resale business
- **Recurring job or decision:** Decide whether a donated or sourced product can legally and safely enter inventory
- **Current workaround:** Inspect the product, manually search CPSC recalls, consult reseller guidance, or discard uncertain items
- **Evidence of friction:** CPSC says resellers are responsible for checking recalls before listing and that recalled products still appear in secondhand channels. The official recall API is machine-readable, but matching depends on incomplete identifiers and free-text descriptions.
- **Frequency:** Per intake item or listing; potentially daily
- **Consequence:** Illegal sale, removal from a marketplace, wasted intake labor, and risk of injury
- **Required inputs:** Product label text, brand, model, product type, optional UPC, and CPSC recall API data
- **Actionable output:** `CLEAR`, `HOLD FOR REVIEW`, or `DO NOT SELL`, with matched recall evidence and the exact attributes requiring confirmation
- **Existing alternatives:** CPSC web search, email alerts, marketplace controls, and general reseller guidance
- **Why a small project might compete:** A focused intake tool could turn label details into evidence-linked candidate matches without requiring a retailer integration
- **Fastest useful experiment:** Sample 50 recall notices across five common resale categories, create realistic label queries, and measure candidate-recall recall/precision plus review time against manual CPSC search
- **Strongest falsification argument:** Recall records may lack stable identifiers often enough that automated matching produces too many false positives; large marketplaces may already solve the valuable portion
- **Evidence references:** EVIDENCE-001, EVIDENCE-002
- **Status:** exploring

| Criterion | 1–5 |
|---|---:|
| Pain | 5 |
| Frequency | 5 |
| User clarity | 5 |
| Actionability | 5 |
| Input access | 5 |
| Existing-alternative gap | 3 |
| Validation feasibility | 5 |
| Buildability | 4 |
| Continuation value | 4 |

**Total:** 41/45

### Candidate: Provider-directory consistency auditor

- **Domain:** Health-plan data operations
- **Specific user:** Provider-directory data or compliance analyst at a regional health plan
- **Recurring job or decision:** Identify records that are stale, contradictory, malformed, or likely to need provider verification before publication
- **Current workaround:** Schema validation, periodic provider outreach, manual comparison with internal rosters, and exception reports
- **Evidence of friction:** CMS requires affected public provider directories and timely updates. Its multi-year review found fewer than half of reviewed listings fully accurate, current, and complete, while noting disagreement between machine-readable files and network directories.
- **Frequency:** Continuous ingestion plus monthly/quarterly verification cycles
- **Consequence:** Members cannot locate care, plan operations absorb rework, and inaccurate directories create compliance exposure
- **Required inputs:** Public payer APIs/files, CMS provider datasets, plan roster exports supplied by a user, and optional provider attestations
- **Actionable output:** Ranked verification queue with field-level discrepancies, freshness evidence, and source provenance
- **Existing alternatives:** Payer master-data systems, CMS validators, provider outreach vendors, and directory-management platforms
- **Why a small project might compete:** An open, source-agnostic discrepancy engine could serve regional plans or consultants without replacing the master system
- **Fastest useful experiment:** Compare two public directory sources and CMS provider data for one geography; manually adjudicate 100 flagged discrepancies
- **Strongest falsification argument:** Public-source disagreement does not establish ground truth, enterprise sales are slow, and existing vendors may already cover the workflow
- **Evidence references:** EVIDENCE-003, EVIDENCE-004
- **Status:** exploring

| Criterion | 1–5 |
|---|---:|
| Pain | 5 |
| Frequency | 5 |
| User clarity | 4 |
| Actionability | 5 |
| Input access | 4 |
| Existing-alternative gap | 3 |
| Validation feasibility | 4 |
| Buildability | 3 |
| Continuation value | 5 |

**Total:** 38/45

### Candidate: Solicitation amendment brief

- **Domain:** Public procurement / small-business operations
- **Specific user:** Proposal lead at a small federal contractor following several active solicitations
- **Recurring job or decision:** Determine what changed in a solicitation or attachment set and whether the bid plan, compliance matrix, or deadline must change
- **Current workaround:** Follow notices in SAM.gov, download revised attachments, manually compare files, and circulate notes
- **Evidence of friction:** Solicitations explicitly place responsibility on offerors to monitor and acknowledge amendments. SAM.gov can follow opportunity changes, but its public search API exposes only the latest active version; historical versions require a separate data route.
- **Frequency:** Each amendment during an active pursuit
- **Consequence:** Missed requirement, nonresponsive bid, rework, or avoidable no-bid decision
- **Required inputs:** Followed SAM.gov opportunity metadata, snapshots or version downloads, and public attachments
- **Actionable output:** Evidence-linked change brief categorized by deadline, scope, submission, pricing, and compliance impact
- **Existing alternatives:** Built-in SAM.gov following, commercial bid platforms, document comparison tools, and proposal consultants
- **Why a small project might compete:** A narrow tool could convert raw revisions into a compliance-oriented brief for small teams
- **Fastest useful experiment:** Backtest ten amended solicitations, manually create ground-truth change lists, and compare tool coverage and review time
- **Strongest falsification argument:** SAM.gov already follows changes, commercial platforms are established, the API requires an account key, and reliably interpreting mixed PDF/Office attachments may be too broad
- **Evidence references:** EVIDENCE-005, EVIDENCE-006
- **Status:** exploring

| Criterion | 1–5 |
|---|---:|
| Pain | 4 |
| Frequency | 5 |
| User clarity | 5 |
| Actionability | 5 |
| Input access | 3 |
| Existing-alternative gap | 2 |
| Validation feasibility | 4 |
| Buildability | 4 |
| Continuation value | 4 |

**Total:** 36/45
