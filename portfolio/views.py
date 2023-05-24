import datetime

from django.shortcuts import render


# Create your views here.

def index_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']

    context = {
        'hora': agora.hour,
        'local': local,
        'topicos': topicos,
    }

    return render(request, 'portfolio/home.html')


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def licenciatura_page_view(request):
    return render(request, 'portfolio/licenciatura.html')


def projetos_page_view(request):
    return render(request, 'portfolio/projetos.html')