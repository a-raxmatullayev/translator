from django.shortcuts import render
from .models import tarjima
from django.views.generic import TemplateView
# Create your views here.


def enuz(request):
    soz = request.GET.get('word','')
    if soz and soz != '':
        natija = tarjima.objects.filter(inglizcha__contains = soz).all()[:10]

    else:
        natija = None

    return render(request, 'enuz.html', {'word': soz, 'natija': natija})


def uzen(request):
    soz = soz = request.GET.get('word','')
    if soz and soz != '':
        natija = tarjima.objects.filter(uzbekcha__contains = soz).all()[:10]

    else:
        natija = None

    return render(request, 'uzen.html', {'word': soz, 'natija': natija})
