# Evidence Ledger

Record public evidence that materially affects candidate selection, implementation, validation, or a factual claim.

## Entry template

### EVIDENCE-000 — [short description]

- **Candidate or component:**
- **Claim tested:**
- **Source:**
- **Source type:** primary | secondary
- **Retrieved:** YYYY-MM-DD
- **Relevant evidence:**
- **Supports or contradicts:**
- **Confidence:** low | medium | high
- **Limitations:**
- **Resulting decision or next test:**

## Entries

### EVIDENCE-001 — Resellers must screen recalled products

- **Candidate or component:** Secondhand recall screener
- **Claim tested:** Small resellers have a consequential item-level recall-screening obligation.
- **Source:** https://www.cpsc.gov/Business--Manufacturing/Business-Education/ResaleThrift-Stores-Information-Center/Stop-Online-Sale-of-Recalled-Products
- **Source type:** primary
- **Retrieved:** 2026-07-10
- **Relevant evidence:** CPSC states that selling or offering a recalled consumer product is unlawful, applies the rule to secondhand online and in-person sales, and instructs resellers to check the recall database before listing.
- **Supports or contradicts:** Supports the existence, consequence, and current manual workflow.
- **Confidence:** high
- **Limitations:** Legal obligation does not prove willingness to pay or that current tools are inadequate.
- **Resulting decision or next test:** Measure manual search time and matching error on real recall records.

### EVIDENCE-002 — Recall data is machine-readable but identifiers vary

- **Candidate or component:** Secondhand recall screener
- **Claim tested:** A prototype can use authoritative public data.
- **Source:** https://www.cpsc.gov/Recalls/CPSC-Recalls-Application-Program-Interface-API-Information
- **Source type:** primary
- **Retrieved:** 2026-07-10
- **Relevant evidence:** CPSC provides REST access to public recall data in JSON or XML with product-name and text-query examples.
- **Supports or contradicts:** Supports input access and buildability.
- **Confidence:** high
- **Limitations:** The page does not establish identifier completeness; older CPSC API guidance says UPCs are present only when available.
- **Resulting decision or next test:** Profile brand, model, UPC, and description coverage before building a matcher.

### EVIDENCE-003 — Provider directories have recurring update requirements

- **Candidate or component:** Provider-directory consistency auditor
- **Claim tested:** Payers face a recurring, time-bounded directory-maintenance job with accessible data.
- **Source:** https://www.cms.gov/priorities/burden-reduction/overview/interoperability/frequently-asked-questions/provider-directory-api
- **Source type:** primary
- **Retrieved:** 2026-07-10
- **Relevant evidence:** CMS says affected payers must expose public provider-directory APIs and make received directory updates available within 30 calendar days.
- **Supports or contradicts:** Supports user clarity, recurrence, and public input access.
- **Confidence:** high
- **Limitations:** Public API availability does not provide authoritative ground truth about whether a provider is practicing or accepting patients.
- **Resulting decision or next test:** Test whether cross-source discrepancies produce a manageable verification queue rather than unresolvable noise.

### EVIDENCE-004 — Historical review found widespread directory inaccuracy

- **Candidate or component:** Provider-directory consistency auditor
- **Claim tested:** Directory accuracy is materially poor rather than a hypothetical concern.
- **Source:** https://www.cms.gov/files/document/2017-2021mrpdsummaryreportfinal508.pdf
- **Source type:** primary
- **Retrieved:** 2026-07-10
- **Relevant evidence:** CMS reported that slightly fewer than half of reviewed network-provider listings across plan years 2017–2021 had accurate, current, and complete contact, location, specialty, and accessibility information.
- **Supports or contradicts:** Supports pain and consequence.
- **Confidence:** medium
- **Limitations:** The review period is historical, methods and directory quality may have changed, and the result should not be treated as a current national rate.
- **Resulting decision or next test:** Seek newer plan-level validation evidence and avoid using this percentage as a current benchmark.

### EVIDENCE-005 — Offerors must monitor amendments

- **Candidate or component:** Solicitation amendment brief
- **Claim tested:** Amendment review is an actionable responsibility for bidders.
- **Source:** https://sam.gov/opp/37845aa2989b4c57a077479ee603936f/view
- **Source type:** primary
- **Retrieved:** 2026-07-10
- **Relevant evidence:** The official notice states that interested bidders are responsible for obtaining the solicitation and acknowledging all amendments.
- **Supports or contradicts:** Supports the recurring job and consequence.
- **Confidence:** medium
- **Limitations:** A single notice demonstrates the requirement for that procurement, not frequency across all solicitations.
- **Resulting decision or next test:** Sample amended opportunities across agencies and quantify attachment/version complexity.

### EVIDENCE-006 — SAM.gov already follows changes; public API has a history gap

- **Candidate or component:** Solicitation amendment brief
- **Claim tested:** A small tool has accessible inputs and an alternative gap.
- **Source:** https://sam.gov/opportunities ; https://open.gsa.gov/api/get-opportunities-public-api/
- **Source type:** primary
- **Retrieved:** 2026-07-10
- **Relevant evidence:** SAM.gov offers saved searches and opportunity-change following. The public Opportunities API requires a personal API key and returns only the latest active version; historical versions require SAM.gov Data Services.
- **Supports or contradicts:** Supports input availability but contradicts a broad notification product and weakens differentiation.
- **Confidence:** high
- **Limitations:** The usability and completeness of built-in notifications and Data Services were not tested.
- **Resulting decision or next test:** Continue only if attachment-level semantic change briefs outperform built-in following enough to justify an additional tool.
