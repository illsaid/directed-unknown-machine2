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
- **Evidence of friction:** CPSC says resellers are responsible for checking recalls before listing and that recalled products still appear in secondhand channels. The official recall API is machine-readable, but a profile of the 100 newest returned records found no populated structured product-model fields and only three populated UPC lists; 57 descriptions mentioned a model, so matching would require text extraction and human confirmation.
- **Frequency:** Per intake item or listing; potentially daily
- **Consequence:** Illegal sale, removal from a marketplace, wasted intake labor, and risk of injury
- **Required inputs:** Product label text, brand, model, product type, optional UPC, and CPSC recall API data
- **Actionable output:** `CLEAR`, `HOLD FOR REVIEW`, or `DO NOT SELL`, with matched recall evidence and the exact attributes requiring confirmation
- **Existing alternatives:** CPSC web search, email alerts, marketplace controls, and general reseller guidance
- **Why a small project might compete:** A focused intake tool could turn label details into evidence-linked candidate matches without requiring a retailer integration
- **Fastest useful experiment:** Extract label-identifying tokens from the 100 profiled notices, create realistic partial-label queries, and measure candidate-recall recall/precision plus review time against manual CPSC search
- **Strongest falsification argument:** Recall records may lack stable identifiers often enough that automated matching produces too many false positives; large marketplaces may already solve the valuable portion
- **Evidence references:** EVIDENCE-001, EVIDENCE-002, EVIDENCE-007
- **Status:** exploring

| Criterion | 1–5 |
|---|---:|
| Pain | 5 |
| Frequency | 5 |
| User clarity | 5 |
| Actionability | 5 |
| Input access | 4 |
| Existing-alternative gap | 3 |
| Validation feasibility | 5 |
| Buildability | 3 |
| Continuation value | 4 |

**Total:** 39/45

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


### Candidate: Step-free transit disruption guard

- **Domain:** Public transit / accessibility
- **Specific user:** Wheelchair user or rider who cannot use stairs and makes recurring Metrorail trips
- **Recurring job or decision:** Decide whether a planned station and transfer path remains step-free before departure
- **Current workaround:** Check elevator status, station pages, alerts, and alternative-route guidance separately; ask station staff for help after encountering an outage
- **Evidence of friction:** WMATA tells riders to check unit location before travel and notes that an outage can prevent exit at the preferred station, requiring a shuttle or a center-platform workaround.
- **Frequency:** Before each rail trip and again when conditions change
- **Consequence:** Stranding, missed appointments, long detours, or dependence on station staff
- **Required inputs:** Station topology, elevator locations, current and planned outage status, and rider origin/destination
- **Actionable output:** `STEP-FREE`, `REROUTE`, or `ASK FOR SHUTTLE`, with the affected path segment and usable alternative
- **Existing alternatives:** WMATA trip planner, elevator-status page, station pages, ELstat scheduled-outage alerts, and general mapping applications
- **Why a small project might compete:** A route-specific check could translate unit-level status into the consequence for one rider's path rather than making the rider interpret several pages
- **Fastest useful experiment:** Model ten station/transfer paths and replay current or historical outages; compare correct route-impact decisions and lookup time with the official status workflow
- **Strongest falsification argument:** Official status pages and alerts may already solve the job, WMATA's API requires registration, and reliable station-level accessibility topology may be difficult to maintain
- **Evidence references:** EVIDENCE-008, EVIDENCE-009
- **Status:** exploring

| Criterion | 1–5 |
|---|---:|
| Pain | 5 |
| Frequency | 4 |
| User clarity | 5 |
| Actionability | 5 |
| Input access | 4 |
| Existing-alternative gap | 1 |
| Validation feasibility | 4 |
| Buildability | 3 |
| Continuation value | 3 |

**Total:** 34/45

### Candidate: Federal comment-opportunity triage

- **Domain:** Public policy / small-organization compliance
- **Specific user:** Policy lead at a small trade association, nonprofit, or technical society covering a narrow issue area
- **Recurring job or decision:** Decide which new federal notices merit review or a comment before the deadline
- **Current workaround:** Keyword alerts and agency newsletters followed by manual reading, docket checks, and deadline tracking
- **Evidence of friction:** Federal Register documents can carry explicit comment deadlines and link to dockets whose supporting documents change. Public APIs expose documents and dockets, but relevance and action still require reading across sources.
- **Frequency:** Daily or weekly monitoring, with deadline-driven action
- **Consequence:** Missed opportunity to represent members, late analysis, or staff time spent on irrelevant notices
- **Required inputs:** FederalRegister.gov public API, Regulations.gov document/docket metadata, saved issue terms, and optional organization-specific criteria
- **Actionable output:** Ranked `IGNORE`, `REVIEW`, or `COMMENT` queue with deadline, affected topic, reason for relevance, docket links, and source excerpts
- **Existing alternatives:** FederalRegister.gov search and subscriptions, Regulations.gov docket alerts, agency lists, Google alerts, and commercial regulatory-intelligence platforms
- **Why a small project might compete:** A narrow, transparent ruleset could provide organization-specific triage without enterprise software or generic alert volume
- **Fastest useful experiment:** Backtest 50 notices for one technical topic against a manually labeled relevance set and compare review time and deadline capture
- **Strongest falsification argument:** Free subscriptions and docket alerts may be sufficient; relevance depends on organization context that public data alone cannot supply; commercial products already serve high-value buyers
- **Evidence references:** EVIDENCE-010, EVIDENCE-011
- **Status:** exploring

| Criterion | 1–5 |
|---|---:|
| Pain | 4 |
| Frequency | 4 |
| User clarity | 5 |
| Actionability | 5 |
| Input access | 5 |
| Existing-alternative gap | 2 |
| Validation feasibility | 4 |
| Buildability | 4 |
| Continuation value | 4 |

**Total:** 37/45
