import random
from django.shortcuts import render
from models import Quote


def random_quote(request):
    quotes = Quote.objects.all()
    if not quotes:
        return render(request, 'quotes/empty.html')
    weighted = [q.weight for q in quotes]
    selected = random.choice(weighted)
    selected.views += 1
    selected.save()
    return render(request, 'quotes/random.html', {'quote': selected})