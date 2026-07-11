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


### EVIDENCE-007 — Recent recall records require text extraction

- **Candidate or component:** Secondhand recall screener
- **Claim tested:** Recent recall notices expose stable, structured identifiers suitable for direct label matching.
- **Source:** https://www.saferproducts.gov/RestWebServices/Recall?format=json
- **Source type:** primary
- **Retrieved:** 2026-07-10
- **Relevant evidence:** A profile of the first 100 records returned by the API, dated 2026-05-07 through 2026-07-09, found product names, descriptions, and images in 100/100 records; structured product-model fields in 0/100; structured UPC lists in 3/100; and the word "model" in 57/100 descriptions.
- **Supports or contradicts:** Contradicts direct structured-identifier matching but supports extraction from descriptions and image captions.
- **Confidence:** high
- **Limitations:** The first 100 API results are a recent convenience sample, not a random sample or a population estimate. Mentioning "model" does not guarantee a complete or visible model number.
- **Resulting decision or next test:** Reduce input-access and buildability scores; test candidate generation from partial label text with mandatory human confirmation.

### EVIDENCE-008 — An elevator outage can invalidate a rider's station path

- **Candidate or component:** Step-free transit disruption guard
- **Claim tested:** Elevator status changes create a consequential trip decision rather than a passive information need.
- **Source:** https://www.wmata.com/ride/elevators-escalators.html
- **Source type:** primary
- **Retrieved:** 2026-07-10
- **Relevant evidence:** WMATA instructs riders to check whether a unit is out, note its location, and plan accordingly; it says an outage can prevent a rider from exiting at the preferred station and may require shuttle service or a center-platform workaround.
- **Supports or contradicts:** Supports pain, actionability, and route-specific consequence.
- **Confidence:** high
- **Limitations:** This establishes the operational consequence, not dissatisfaction with WMATA's existing tools.
- **Resulting decision or next test:** Test whether path-level interpretation saves time or catches impacts that the official workflow leaves to the rider.

### EVIDENCE-009 — Official transit status data exists but requires registration

- **Candidate or component:** Step-free transit disruption guard
- **Claim tested:** Current elevator status and station data are programmatically accessible.
- **Source:** https://www.wmata.com/about/developers.html
- **Source type:** primary
- **Retrieved:** 2026-07-10
- **Relevant evidence:** WMATA says its API includes station information, service alerts, and elevator/escalator status, and that developers must register for an official API key.
- **Supports or contradicts:** Supports buildability while weakening frictionless input access.
- **Confidence:** high
- **Limitations:** Endpoint completeness, latency, station topology, and historical availability were not tested because no account was created.
- **Resulting decision or next test:** Before shortlisting, verify whether unauthenticated GTFS accessibility fields plus published status are sufficient for a reproducible prototype.

### EVIDENCE-010 — Federal Register offers keyless public document APIs

- **Candidate or component:** Federal comment-opportunity triage
- **Claim tested:** New notices and their metadata can be monitored without a private feed.
- **Source:** https://www.federalregister.gov/developers/documentation/api/v1
- **Source type:** primary
- **Retrieved:** 2026-07-10
- **Relevant evidence:** FederalRegister.gov documents multiple public API endpoints and states that no API key is required.
- **Supports or contradicts:** Supports input access and low prototype operating burden.
- **Confidence:** high
- **Limitations:** FederalRegister.gov is an unofficial informational rendition; legally consequential results must link to the official edition.
- **Resulting decision or next test:** Backtest deadline extraction and relevance triage while retaining official-document links.

### EVIDENCE-011 — Docket data is searchable, but incumbents already alert

- **Candidate or component:** Federal comment-opportunity triage
- **Claim tested:** A small tool can inspect docket changes and has an alternative gap.
- **Source:** https://open.gsa.gov/api/regulationsgov/ ; https://downloads.regulations.gov/NRC-2019-0062-0012/content.pdf
- **Source type:** primary
- **Retrieved:** 2026-07-10
- **Relevant evidence:** Regulations.gov provides search APIs for documents, comments, and dockets, using an API key with DEMO_KEY allowed for samples. An official notice describes Regulations.gov docket alerts for changes or additions with daily, weekly, or monthly delivery.
- **Supports or contradicts:** Supports accessible inputs but contradicts a generic monitoring product.
- **Confidence:** high
- **Limitations:** Alert usability and coverage were not directly tested, and the cited alert instructions are from one agency notice.
- **Resulting decision or next test:** Continue only as relevance-and-action triage demonstrably better than existing alerts, not as another notification feed.
