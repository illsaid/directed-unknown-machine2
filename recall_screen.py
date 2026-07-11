#!/usr/bin/env python3
"""Conservative CPSC recall candidate screener for secondhand intake."""

from __future__ import annotations

import argparse
import json
import re
import urllib.request
from pathlib import Path

CPSC_URL = "https://www.saferproducts.gov/RestWebServices/Recall?format=json"
DISCLAIMER = (
    "This is candidate screening, not legal or safety clearance. "
    "No candidate found does not mean the product has not been recalled."
)
TOKEN_RE = re.compile(r"[A-Za-z0-9]+(?:[-_./][A-Za-z0-9]+)*")


def normalize(value: object) -> str:
    return re.sub(r"[^a-z0-9]", "", str(value or "").lower())


def words(value: object) -> set[str]:
    return {normalize(token) for token in TOKEN_RE.findall(str(value or "")) if len(normalize(token)) > 1}


def nested_values(record: dict) -> list[str]:
    values = [str(record.get("Title") or ""), str(record.get("Description") or "")]
    for field in ("Products", "ProductUPCs", "Images", "Manufacturers", "Importers", "Distributors"):
        for item in record.get(field) or []:
            if isinstance(item, dict):
                values.extend(str(value) for value in item.values() if value is not None)
            elif item is not None:
                values.append(str(item))
    return values


def record_tokens(record: dict) -> set[str]:
    tokens: set[str] = set()
    for value in nested_values(record):
        tokens.update(words(value))
    return tokens


def record_text(record: dict) -> str:
    return normalize(" ".join(nested_values(record)))


def rank_record(record: dict, *, brand: str, model: str, upc: str, product: str) -> dict | None:
    tokens = record_tokens(record)
    text = record_text(record)
    reasons: list[str] = []
    score = 0
    exact_identity = False

    upc_key = normalize(upc)
    if upc_key and upc_key in tokens:
        score += 120
        reasons.append("exact UPC")
        exact_identity = True

    model_key = normalize(model)
    normalized_tokens = {normalize(token) for token in tokens}
    if model_key and model_key in normalized_tokens:
        score += 100
        reasons.append("exact model token")
        exact_identity = True
    elif len(model_key) >= 5 and model_key in text:
        score += 70
        reasons.append("partial model text")

    if not reasons:
        return None

    brand_terms = words(brand)
    brand_hits = sorted(brand_terms & normalized_tokens)
    if brand_hits:
        score += min(15, 5 * len(brand_hits))
        reasons.append("brand: " + ", ".join(brand_hits))

    product_terms = words(product)
    product_hits = sorted(product_terms & normalized_tokens)
    if product_hits:
        score += min(10, 2 * len(product_hits))
        reasons.append("product: " + ", ".join(product_hits))

    return {
        "score": score,
        "exact_identity": exact_identity,
        "recall_id": record.get("RecallID"),
        "recall_number": record.get("RecallNumber"),
        "title": record.get("Title"),
        "url": record.get("URL"),
        "matched": reasons,
        "hazards": [item.get("Name") for item in record.get("Hazards") or [] if item.get("Name")],
        "remedies": [item.get("Name") for item in record.get("Remedies") or [] if item.get("Name")],
    }


def screen(records: list[dict], *, brand: str = "", model: str = "", upc: str = "", product: str = "") -> dict:
    if not normalize(model) and not normalize(upc):
        return {
            "outcome": "INSUFFICIENT IDENTITY",
            "candidates": [],
            "next_step": "Locate and enter a model number or UPC; otherwise perform manual CPSC review.",
            "disclaimer": DISCLAIMER,
        }

    candidates = [
        candidate
        for record in records
        if (candidate := rank_record(record, brand=brand, model=model, upc=upc, product=product))
    ]
    candidates.sort(key=lambda item: (-item["score"], str(item["recall_id"])))
    candidates = candidates[:5]

    if not candidates:
        outcome = "NO CANDIDATE FOUND \u2014 NOT A CLEARANCE"
        next_step = "Try alternate label text and manually review CPSC records before listing."
    elif candidates[0]["exact_identity"] and (
        len(candidates) == 1 or candidates[0]["score"] > candidates[1]["score"]
    ):
        outcome = "MATCHED RECALL \u2014 HOLD"
        next_step = "Hold the item and confirm every identifying detail against the official recall notice."
    else:
        outcome = "POSSIBLE MATCH \u2014 HOLD"
        next_step = "Hold the item and resolve ambiguous or partial matches against official notices."

    for candidate in candidates:
        candidate.pop("exact_identity", None)
    return {"outcome": outcome, "candidates": candidates, "next_step": next_step, "disclaimer": DISCLAIMER}


def load_records(path: Path | None, refresh: bool = False) -> list[dict]:
    cache = path or Path(".cache/cpsc_recalls.json")
    if refresh or not cache.exists():
        cache.parent.mkdir(parents=True, exist_ok=True)
        request = urllib.request.Request(CPSC_URL, headers={"User-Agent": "DirectedUnknownMachine/2"})
        with urllib.request.urlopen(request, timeout=120) as response:
            data = response.read()
        json.loads(data)
        cache.write_bytes(data)
    with cache.open(encoding="utf-8") as handle:
        records = json.load(handle)
    if not isinstance(records, list):
        raise ValueError("Recall data must be a JSON list")
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--brand", default="")
    parser.add_argument("--model", default="")
    parser.add_argument("--upc", default="")
    parser.add_argument("--product", default="")
    parser.add_argument("--data", type=Path, help="JSON file; defaults to a downloaded local cache")
    parser.add_argument("--refresh", action="store_true", help="refresh the configured data cache")
    args = parser.parse_args()
    result = screen(
        load_records(args.data, args.refresh),
        brand=args.brand,
        model=args.model,
        upc=args.upc,
        product=args.product,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
