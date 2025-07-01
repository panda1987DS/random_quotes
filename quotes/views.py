import random
from django.shortcuts import render, redirect
from .models import Quote
from .forms import QuoteForm


def random_quote(request):
    quotes = Quote.objects.all()
    if not quotes:
        return render(request, 'empty.html')
    weights = [q.weight for q in quotes]
    selected = random.choices(quotes, weights=weights, k=1)[0]
    selected.views += 1
    selected.save()
    return render(request, 'random.html', {'quote': selected})


def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('random_quote')
    else:
        form = QuoteForm()
    return render(request, 'add.html', {'add': form})