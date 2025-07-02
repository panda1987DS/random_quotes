from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    """
       Form for creating and editing Quote instances.

       When editing an existing quote, the 'text' and 'source' fields are disabled (read-only).
       The form validates:
       - No more than 3 quotes can come from the same source (on creation).
       - Duplicate quotes (same text and source) are not allowed (on creation).
    """

    class Meta:
        model = Quote
        fields = ['text', 'source', 'weight']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['text'].disabled = True
            self.fields['source'].disabled = True

    def clean(self):
        cleaned_data = super().clean()
        source = cleaned_data.get('source')
        text = cleaned_data.get('text')

        if not source or not text:
            return cleaned_data

        existing = Quote.objects.filter(source=source, text=text)
        if self.instance.pk:
            existing = existing.exclude(pk=self.instance.pk)

        if source and not self.instance.pk and Quote.objects.filter(source=source).count() >= 3:
            raise forms.ValidationError("Уже есть 3 цитаты из этого источника.")

        if not self.instance.pk and existing.exists():
            raise forms.ValidationError("Такая цитата уже существует.")

        return cleaned_data
