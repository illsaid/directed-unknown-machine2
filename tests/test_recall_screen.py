import unittest

from recall_screen import screen


def recall(recall_id, title, description, *, upc=""):
    return {
        "RecallID": recall_id,
        "RecallNumber": str(recall_id),
        "Title": title,
        "Description": description,
        "URL": f"https://www.cpsc.gov/Recalls/{recall_id}",
        "Products": [{"Name": title, "Model": ""}],
        "ProductUPCs": [{"UPC": upc}] if upc else [],
        "Images": [],
        "Manufacturers": [],
        "Importers": [],
        "Distributors": [],
        "Hazards": [{"Name": "Fire hazard"}],
        "Remedies": [{"Name": "Stop use and contact the firm"}],
    }


RECORDS = [
    recall(1, "Insignia gas ranges", "Models NS-RGFGSS1 and NS-RGFCGS2"),
    recall(2, "Alpha heater", "Model ABC-1234-X"),
    recall(3, "Alpha fan", "Model ABC-1234-Y"),
    recall(4, "Beta lamp", "Table lamp", upc="012345678905"),
]


class ScreenTests(unittest.TestCase):
    def test_exact_model_returns_evidence_linked_hold(self):
        result = screen(RECORDS, brand="Insignia", model="NS-RGFGSS1", product="gas range")
        self.assertEqual(result["outcome"], "MATCHED RECALL \u2014 HOLD")
        self.assertEqual(result["candidates"][0]["recall_id"], 1)
        self.assertTrue(result["candidates"][0]["url"].startswith("https://www.cpsc.gov/"))

    def test_partial_model_is_conservative(self):
        result = screen(RECORDS, model="NS-RGFGS")
        self.assertEqual(result["outcome"], "POSSIBLE MATCH \u2014 HOLD")
        self.assertEqual(result["candidates"][0]["recall_id"], 1)

    def test_ambiguous_partial_model_keeps_multiple_candidates(self):
        result = screen(RECORDS, model="ABC1234")
        self.assertEqual(result["outcome"], "POSSIBLE MATCH \u2014 HOLD")
        self.assertEqual({item["recall_id"] for item in result["candidates"]}, {2, 3})

    def test_exact_upc_matches(self):
        result = screen(RECORDS, upc="0 12345 67890 5", product="lamp")
        self.assertEqual(result["outcome"], "MATCHED RECALL \u2014 HOLD")
        self.assertEqual(result["candidates"][0]["recall_id"], 4)

    def test_missing_identifier_is_insufficient(self):
        result = screen(RECORDS, brand="Insignia", product="range")
        self.assertEqual(result["outcome"], "INSUFFICIENT IDENTITY")
        self.assertEqual(result["candidates"], [])

    def test_no_candidate_never_claims_clearance(self):
        result = screen(RECORDS, model="ZZZ-9999")
        self.assertEqual(result["outcome"], "NO CANDIDATE FOUND \u2014 NOT A CLEARANCE")
        self.assertIn("not legal or safety clearance", result["disclaimer"])

    def test_null_fields_in_official_records_do_not_crash(self):
        record = recall(5, "Old product", "Model NULL-100")
        record["Title"] = None
        record["Description"] = None
        result = screen(RECORDS + [record], model="NS-RGFGSS1")
        self.assertEqual(result["outcome"], "MATCHED RECALL \u2014 HOLD")


if __name__ == "__main__":
    unittest.main()
