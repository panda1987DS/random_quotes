import random
from django.shortcuts import render, redirect
from .models import Quote
from .forms import QuoteForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST

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

@require_POST
def like_quote(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    quote.likes += 1
    quote.save()
    return JsonResponse({'likes': quote.likes})

@require_POST
def dislike_quote(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    quote.dislikes += 1
    quote.save()
    return JsonResponse({'dislikes': quote.dislikes})