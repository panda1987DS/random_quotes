"""
Views for the quote application.

Includes functionality for:
- displaying a random quote
- adding, editing, deleting quotes
- liking/disliking quotes
- showing top quotes with sorting and filtering
"""

import random

from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
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
            try:
                form.save()
                return redirect('random_quote')
            except form.ValidationError as e:
                form.add_error(None, e)
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


def top_quotes(request):
    sort_param = request.GET.get('sort', 'likes')
    limit = request.GET.get('limit', '10')
    source_filter = request.GET.get('source', '').strip()

    try:
        limit = int(limit)
    except ValueError:
        limit = 10

    quotes = Quote.objects.all()

    if source_filter:
        quotes = quotes.filter(source__icontains=source_filter)

    if sort_param == 'likes':
        quotes = quotes.order_by('-likes')
    elif sort_param == 'dislikes':
        quotes = quotes.order_by('-dislikes')
    elif sort_param == 'diff':
        quotes = quotes.annotate(diff=F('likes') - F('dislikes')).order_by('-diff')
    elif sort_param == 'views':
        quotes = quotes.order_by('-views')
    else:
        quotes = quotes.order_by('-likes')

    quotes = quotes[:limit]

    limits = [5, 10, 15, 20]
    return render(request, 'top.html', {
        'quotes': quotes,
        'limits': limits,
        'current_limit': limit,
        'current_sort': sort_param,
        'current_source': source_filter,
    })


def edit_quote(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid():
            form.save()
            return redirect('top_quotes')
    else:
        form = QuoteForm(instance=quote)
    return render(request, 'edit.html', {'form': form, 'quote': quote})


@require_POST
def delete_quote(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    quote.delete()
    print(quote)
    return redirect('top_quotes')
