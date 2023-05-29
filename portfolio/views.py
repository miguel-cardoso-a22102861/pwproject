from audioop import reverse
import datetime
from django.http import HttpResponseRedirect

from django.shortcuts import render
from .models import Tarefa
from .forms import TarefaForm


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


def tarefas_page_view(request):
    tarefas = Tarefa.objects.all()

    context = {
        'tarefas': tarefas,
    }

    return render(request, 'portfolio/tarefas.html', context)

def post_page_view(request):
    return render(request, 'portfolio/post.html')


def tarefasNova_page_view(request):
    form = TarefaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:home'))
    

    context = {'form': form}

    return render(request, 'portfolio/tarefasNova.html', context)

def edita_tarefa_view(request, tarefa_id):
    Tarefa.objects.get(id=tarefa_id).clean()

def apaga_tarefa_view(request, tarefa_id):
    Tarefa.objects.get(id=tarefa_id).delete()
    return HttpResponseRedirect(reverse('portfolio:tarefas'))

def post_novo_page_view(request):
    form = TarefaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:home'))
    

    context = {'form': form}

    return render(request, 'portfolio/tarefasNova.html', context)

def edita_tarefa_view(request, tarefa_id):
    Tarefa.objects.get(id=tarefa_id).clean()

def apaga_tarefa_view(request, tarefa_id):
    Tarefa.objects.get(id=tarefa_id).delete()
    return HttpResponseRedirect(reverse('portfolio:tarefas'))