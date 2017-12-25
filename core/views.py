from django.shortcuts import render

# Create your views here.


def base(request):
    return render(request, 'core/base.html')


def home(request):
    return render(request, 'core/home.html')


def tabela(request):
    return render(request, 'core/tabela.html')
