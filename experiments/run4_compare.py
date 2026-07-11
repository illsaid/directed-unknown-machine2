#!/usr/bin/env python3
"""Reproduce the Run 4 public-data comparison without private inputs."""

import concurrent.futures
import json
import re
import urllib.parse
import urllib.request

HEADERS = {"User-Agent": "DirectedUnknownMachine/2 public-research"}
CPSC_URL = "https://www.saferproducts.gov/RestWebServices/Recall?format=json"
FR_URL = (
    "https://www.federalregister.gov/api/v1/documents.json?"
    "per_page=200&order=newest&conditions%5Btype%5D%5B%5D=PRORULE"
)
STOP_TOKENS = {"NUMBER", "NUMBERS", "MODEL", "MODELS", "SHOWN", "LOCATED", "SERIAL"}
PROFILE_TERMS = ("accessibility", "disability", "disabled", "assistive", "wheelchair", "screen reader")


def get_json(url):
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=90) as response:
        return json.load(response)


def caption_model(record):
    for image in record.get("Images") or []:
        caption = image.get("Caption", "")
        for marker in re.finditer(
            r"\bmodels?(?:\s+numbers?)?\s*(?:are|include|:|#)?\s*([^.;]{1,100})",
            caption,
            re.IGNORECASE,
        ):
            for token in re.findall(r"\b[A-Z0-9][A-Z0-9./_-]{2,}\b", marker.group(1).upper()):
                token = token.strip(".,;:()[]")
                if (
                    token not in STOP_TOKENS
                    and any(char.isalpha() for char in token)
                    and any(char.isdigit() for char in token)
                ):
                    return token
    return None


def cpsc_query(case):
    recall_id, full, partial = case
    results = {}
    for label, value in (("exact", full), ("partial", partial)):
        url = CPSC_URL + "&" + urllib.parse.urlencode({"RecallDescription": value})
        matches = get_json(url)
        ids = {item["RecallID"] for item in matches}
        results[label] = {
            "matches": len(matches),
            "target_retrieved": recall_id in ids,
            "target_unique": recall_id in ids and len(matches) == 1,
        }
    return results


def count_query_results(results, key):
    return {
        "target_retrieved": sum(item[key]["target_retrieved"] for item in results),
        "target_unique": sum(item[key]["target_unique"] for item in results),
        "target_ambiguous": sum(
            item[key]["target_retrieved"] and not item[key]["target_unique"] for item in results
        ),
        "target_missed": sum(not item[key]["target_retrieved"] for item in results),
    }


def main():
    recalls = get_json(CPSC_URL)[:100]
    cases = []
    for record in recalls:
        model = caption_model(record)
        if model:
            trim = 2 if len(model) > 6 else 1
            cases.append((record["RecallID"], model, model[:-trim]))
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        recall_results = list(executor.map(cpsc_query, cases))

    proposed_rules = get_json(FR_URL)["results"]
    title_hits = []
    expanded_hits = []
    for document in proposed_rules:
        title = document.get("title", "").lower()
        expanded = (document.get("title", "") + " " + (document.get("abstract") or "")).lower()
        if any(term in title for term in PROFILE_TERMS):
            title_hits.append(document["document_number"])
        if any(term in expanded for term in PROFILE_TERMS):
            expanded_hits.append(document["document_number"])

    output = {
        "method": {
            "recall": "First 100 API records; extract one model-like token from an image caption as a proxy for a physical label; query the official description search with the full token and a token missing its last one or two characters.",
            "federal": "First 200 proposed-rule list records; apply a fixed disability-access profile to title alone and title plus abstract. No independent relevance labels exist.",
        },
        "recall": {
            "records": len(recalls),
            "caption_model_cases": len(cases),
            "exact_official_search": count_query_results(recall_results, "exact"),
            "partial_official_search": count_query_results(recall_results, "partial"),
            "ground_truth": "recall ID associated with the source image caption",
        },
        "federal": {
            "records": len(proposed_rules),
            "profile_terms": list(PROFILE_TERMS),
            "title_keyword_hits": len(title_hits),
            "title_or_abstract_keyword_hits": len(expanded_hits),
            "added_by_abstract": len(set(expanded_hits) - set(title_hits)),
            "independent_relevance_labels": False,
            "advantage_over_official_full_text_alerts_measured": False,
        },
        "limitations": [
            "The recall labels are proxies extracted from recall image captions, not photographs supplied by resellers.",
            "Exact identifier search is already available from the official CPSC API, so this test establishes automatable triage, not superiority over manual search.",
            "The federal profile is synthetic and keyword expansion is not an independent relevance judgment.",
        ],
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()