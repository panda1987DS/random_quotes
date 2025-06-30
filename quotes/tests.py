from django.test import TestCase
from quotes.models import Quote


class QuoteTests(TestCase):
    def test_add_unique_quote(self):
        Quote.objects.create(text="text", source="source", weight=1)
        self.assertEqual(Quote.objects.count(), 1)

    def test_duplicate_quote_not_allowed(self):
        Quote.objects.create(text="text", source="source", weight=1)
        with self.assertRaises(Exception):
            Quote.objects.create(text="text", source="source", weight=2)

    def test_source_limit(self):
        Quote.objects.create(text="1", source="source", weight=1)
        Quote.objects.create(text="2", source="source", weight=1)
        Quote.objects.create(text="3", source="source", weight=1)
        with self.assertRaises(Exception):
            Quote.objects.create(text="4", source="source", weight=1)
