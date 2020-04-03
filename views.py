from django.shortcuts import get_object_or_404, render
from .wineforms import WineForm
import datetime

# Create your views here.
from wine.models import Wine, Tag


def index(request):
    stocked_wine_list = Wine.objects.filter(quantity__gt=0).order_by("name")
    total_value = sum([item.price for item in stocked_wine_list])
    context = {
        'stocked_wine_list': stocked_wine_list,
        'total_value': total_value
    }
    return render(request, 'wine/index.html', context)


def detail(request, wine_id):
    wine = get_object_or_404(Wine, pk=wine_id)
    if wine.score == 0:
        wine.score = "Not set"
    tags = wine.tags.all().values_list('name', flat=True)
    taglist = list(tags)
    data = {'score': wine.score,
            'comments': wine.comments,
            'tags': ",".join(taglist)}
    form = WineForm(data)
    context = {
        'wine': wine,
        'form': form
    }
    return render(request, 'wine/detail.html', context)


def drank(request, wine_id):
    form = WineForm(request.POST)
    if form.is_valid():
        wine = Wine.objects.get(pk=wine_id)
        if wine.quantity > 0:
            wine.quantity -= 1
            wine.consumed += 1
            wine.last_drank_date = datetime.datetime.now()
        wine.comments = form.cleaned_data['comments']
        wine.score = form.cleaned_data['score']
        tags = form.cleaned_data['tags'].split(",")
        tags = [x.strip() for x in tags]
        tags_legit = [x for x in tags if x != ""]
        if len(tags_legit) > 0:
            for tag in tags_legit:
                dbtag, created = Tag.objects.get_or_create(name=tag)
                wine.tags.add(dbtag)
        wine.save()

    return detail(request, wine_id)


def recent(request):
    wines = Wine.objects.filter(consumed__gt=0).order_by('-last_drank_date')
    context = {
        'wines': wines
    }
    return render(request, 'wine/recent.html', context)
