from django.urls import reverse
import datetime
from django.http import HttpResponseRedirect

from django.shortcuts import redirect, render
from .models import Post, Tarefa, TecnologiasPW
from .forms import PostForm, TarefaForm


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

def postNovo_page_view(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('portfolio:blog')
    
    

    context = {'form': form}

    return render(request, 'portfolio/blogNovo.html', context)
        


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

def post_apaga_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))

def post_edita_view(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        context = {'form': form, 'post_id': post_id}
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}

               

    return render(request, 'portfolio/blogEdita.html', context)


def blog_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'portfolio/blog.html', context)


def tecnologiasUsadas_view(request):
    tecnologiasUsadas = TecnologiasPW.objects.all()
    context = {
        'tecnologiasUsadas': tecnologiasUsadas,
    }

    return render(request, 'portfolio/tecnologiasUsadas.html', context)

