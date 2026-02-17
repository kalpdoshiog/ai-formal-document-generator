"""
Basic tests for the generator app.
"""
from unittest.mock import patch, MagicMock

from django.test import TestCase, Client
from django.urls import reverse

from .models import DocumentLog
from .constants import DESIGNATION_MAP
from .views.helpers import format_date_ddmmyyyy, safe_designation


# ------------------------------------------------------------------
# Helper unit tests
# ------------------------------------------------------------------
class HelperTests(TestCase):
    def test_format_date_valid(self):
        self.assertEqual(format_date_ddmmyyyy("2026-02-16"), "16-02-2026")

    def test_format_date_invalid(self):
        self.assertEqual(format_date_ddmmyyyy("not-a-date"), "not-a-date")

    def test_format_date_empty(self):
        self.assertEqual(format_date_ddmmyyyy(""), "")

    def test_safe_designation_valid(self):
        result = safe_designation("Director General", "en")
        self.assertEqual(result, "Director General")

    def test_safe_designation_hindi(self):
        result = safe_designation("Director General", "hi")
        self.assertEqual(result, "महानिदेशक")

    def test_safe_designation_missing_key(self):
        result = safe_designation("NonExistentPosition", "en")
        self.assertEqual(result, "NonExistentPosition")

    def test_safe_designation_none_key(self):
        result = safe_designation(None, "en")
        self.assertEqual(result, "")


# ------------------------------------------------------------------
# Model tests
# ------------------------------------------------------------------
class DocumentLogModelTests(TestCase):
    def test_create_document_log(self):
        log = DocumentLog.objects.create(
            document_type="Office Order",
            language="en",
            reference_id="TEST-001",
            content="Test body content",
        )
        self.assertEqual(str(log), "Office Order | TEST-001")
        self.assertEqual(DocumentLog.objects.count(), 1)

    def test_document_type_choices(self):
        types = [choice[0] for choice in DocumentLog.DOCUMENT_TYPES]
        self.assertIn("Office Order", types)
        self.assertIn("Circular", types)
        self.assertIn("Policy", types)


# ------------------------------------------------------------------
# View / URL tests
# ------------------------------------------------------------------
class HomeViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BISAG-N Document Generator")

    def test_home_contains_designations(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Director General")


class OfficeOrderViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_generate_body_get_not_allowed(self):
        response = self.client.get(reverse("generate_body"))
        self.assertEqual(response.status_code, 400)

    @patch("generator.views.office_order.get_gemini_model")
    def test_generate_body_post(self, mock_get_model):
        mock_model = MagicMock()
        mock_model.generate_content.return_value = MagicMock(text="Generated body text")
        mock_get_model.return_value = mock_model

        response = self.client.post(reverse("generate_body"), {
            "body_prompt": "Test prompt",
            "language": "en",
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Generated body text")

    def test_result_office_order_get_redirects(self):
        response = self.client.get(reverse("result"))
        self.assertEqual(response.status_code, 302)

    def test_result_office_order_post(self):
        response = self.client.post(reverse("result"), {
            "language": "en",
            "date": "2026-02-16",
            "reference": "BISAG-N/Test/2026/",
            "body": "Test body",
            "from_position": "Director General",
            "to_recipients[]": ["Senior Manager"],
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(DocumentLog.objects.count(), 1)

    def test_download_pdf_no_session(self):
        response = self.client.get(reverse("download_pdf"))
        self.assertEqual(response.status_code, 400)

    def test_download_docx_no_session(self):
        response = self.client.get(reverse("download_docx"))
        self.assertEqual(response.status_code, 400)


class CircularViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_generate_circular_body_get_not_allowed(self):
        response = self.client.get(reverse("generate_circular_body"))
        self.assertEqual(response.status_code, 400)

    def test_result_circular_get_redirects(self):
        response = self.client.get(reverse("result_circular"))
        self.assertEqual(response.status_code, 302)


class PolicyViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_generate_policy_body_get_not_allowed(self):
        response = self.client.get(reverse("generate_policy_body"))
        self.assertEqual(response.status_code, 400)

    def test_result_policy_get_redirects(self):
        response = self.client.get(reverse("result_policy"))
        self.assertEqual(response.status_code, 302)


# ------------------------------------------------------------------
# Constants tests
# ------------------------------------------------------------------
class ConstantsTests(TestCase):
    def test_designation_map_has_entries(self):
        self.assertGreater(len(DESIGNATION_MAP), 0)

    def test_each_designation_has_en_and_hi(self):
        for key, value in DESIGNATION_MAP.items():
            self.assertIn("en", value, f"Missing 'en' for {key}")
            self.assertIn("hi", value, f"Missing 'hi' for {key}")

    def test_no_tab_in_values(self):
        """Ensure no stray tab characters in designation values."""
        for key, value in DESIGNATION_MAP.items():
            for lang, text in value.items():
                self.assertNotIn("\t", text, f"Tab character found in {key}[{lang}]")
