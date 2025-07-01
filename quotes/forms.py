from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'source', 'weight']

    def clean(self):
        cleaned_data = super().clean()
        source = cleaned_data.get('source')
        text = cleaned_data.get('text')

        if source and Quote.objects.filter(source=source).count() >= 3:
            raise forms.ValidationError("Уже есть 3 цитаты из этого источника.")

        if source and text and Quote.objects.filter(source=source, text=text).exists():
            raise forms.ValidationError("Такая цитата уже существует.")

        return cleaned_data
