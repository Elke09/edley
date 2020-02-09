from django.shortcuts import render
from django.http import HttpResponse
from .models import TelefonbuchEintrag
# Create your views here.

def hello(request):
    return HttpResponse('hello world!')

def einträge(request):
    einträge = TelefonbuchEintrag.objects.all()
    return render(request, 'einträge.html', context= {'einträge': einträge})
