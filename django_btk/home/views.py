from django.http import HttpResponseRedirect
from django.shortcuts import render
from home.models import Setting
from product.models import Category, Product


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'home'}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'referanslar'}
    return render(request, 'referanslar.html', context)

def iletisim(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'iletisim'}
    return render(request, 'iletisim.html', context)

def shop(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'shop'}
    return render(request, 'shop.html', context)

def detail(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'detail'}
    return render(request, 'detail.html', context)