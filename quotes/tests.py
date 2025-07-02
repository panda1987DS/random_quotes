from django.test import TestCase

from quotes.forms import QuoteForm
from quotes.models import Quote


class QuoteTests(TestCase):
    def setUp(self):
        Quote.objects.create(text="0", source="1", weight=1)

    def test_duplicate_quote_not_allowed(self):
        data = {
            "text": "0",
            "source": "1",
            "weight": 2
        }
        form = QuoteForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("__all__", form.errors)
        self.assertIn("Такая цитата уже существует", form.errors["__all__"][0])

    def test_source_limit(self):
        Quote.objects.create(text="1", source="1", weight=1)
        Quote.objects.create(text="2", source="1", weight=2)
        Quote.objects.create(text="3", source="1", weight=3)

        data = {"text": "4", "source": "1", "weight": 4}
        form = QuoteForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("Уже есть 3 цитаты из этого источника.", form.errors["__all__"][0])
