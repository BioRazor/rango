from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict={'boldmessage': 'Here is the boldmessage'}

    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'title' : 'About Rango', 'variable' : 'Here a context variable'}

    return render(request, 'rango/about.html', context = context_dict)
