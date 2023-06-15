import base64
import io
from django.urls import reverse
import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, redirect, render
from .models import AptidoesCompetencias, Cadeira, CadeiraV2, CursoModelo, Educacao, PadroesUsados, Pessoa, PontuacaoQuizz, Projeto, SobreWebsite, TecnologiasExistentesPW, TfcsInteressantes, LaboratoriosPW, NoticiasPW, Post, Tarefa, TecnologiasPW
from .forms import CadeiraForm, PostForm, ProjetoForm, TarefaForm, TfcsInteressantesForm

from matplotlib import pyplot as plt
import urllib
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

@login_required
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



@login_required(login_url="/accounts/login")

def edita_tarefa_view(request, tarefa_id):
    Tarefa.objects.get(id=tarefa_id).clean()

@login_required(login_url="/accounts/login")
def apaga_tarefa_view(request, tarefa_id):
    Tarefa.objects.get(id=tarefa_id).delete()
    return HttpResponseRedirect(reverse('portfolio:tarefas'))

@login_required(login_url="/accounts/login")

def post_apaga_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))

@login_required(login_url="/accounts/login")
def post_edita_view(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        context = {'form': form, 'post_id': post_id}
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}

               

    return render(request, 'portfolio/blogEdita.html', context)

@login_required(login_url="/accounts/login")
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

def laboratorios_view(request):
    laboratorios = LaboratoriosPW.objects.all()
    context = {
        'laboratorios': laboratorios,
    }
    return render(request, 'portfolio/laboratorios.html', context)

def noticiasPW_view(request):

    noticiasPW = NoticiasPW.objects.all()
    context = {
        'noticiasPW': noticiasPW,
    }

    return render(request, 'portfolio/noticiasPW.html', context)



def tfcsInteresssantes_view(request):

    tfcsInteressantes = TfcsInteressantes.objects.all()
    context = {
        'tfcsInteressantes': tfcsInteressantes,
    }

    return render(request, 'portfolio/tfcsInteresssantes.html', context)

def projetosPessoais_view(request):

    projetosPessoais = Projeto.objects.all()
    context = {
        'projetosPessoais': projetosPessoais,
    }

    return render(request, 'portfolio/projetosPessoais.html', context)

def pessoas_view(request):

    pessoas = Pessoa.objects.all()
    context = {
        'pessoas': pessoas,
    }
    return render(request, context)

def aptidoesCompetencias_view(request):

    aptidoesCompetencias = AptidoesCompetencias.objects.all()
    context = {
        'aptidoesCompetencias': aptidoesCompetencias,
    }
    return render(request, 'portfolio/aptidoesCompetencias.html', context)

def licenciatura_view(request):
    cadeiras = CadeiraV2.objects.all()
    context = {
        'cadeiras': cadeiras,
    }
    return render(request, 'portfolio/licenciatura.html', context)


def cadeiraDetalhes_view(request, pk):
    cadeira = get_object_or_404(CadeiraV2, pk=pk)
    return render(request, 'cadeira_detail.html', {'cadeira': cadeira})



def playground_view(request):


    return render(request, 'portfolio/playground.html')


def contactos_view(request):

    return render(request, 'portfolio/contactos.html')


def educacao_view(request):
    educacoes = Educacao.objects.all()
    context = {
       'educacoes':educacoes,
       
   }

    return render(request, 'portfolio/educacao.html', context)




def experienciaProfissional_view(request):
    
    return render(request, 'portfolio/experienciaProfissional.html')

def interesses_view(request):

    return render(request, 'portfolio/interesses.html' )



def projetosUniversidade_view(request):
   
   projetosUniversidade = Projeto.objects.all()

   context = {
       'projetosUniversidade':projetosUniversidade,
       
   }
   return render(request, 'portfolio/projetosUniversidade.html', context)



def tecnologiasExistentes_view(request):
    tecnologiasExistentes = TecnologiasExistentesPW.objects.all()
    context = {
        'tecnologiasExistentes': tecnologiasExistentes,
    }

    return render(request, 'portfolio/tecnologiasExistentes.html', context)

def noticiasPW_view(request):
    noticiasPW = NoticiasPW.objects.all()
    context = {
        'noticiasPW': noticiasPW,
    }

    return render(request, 'portfolio/noticiasPW.html', context)

def sobreWebsite_view(request):
    sobreWebsite = SobreWebsite.objects.all()
    context = {
        'sobreWebsite': sobreWebsite,
    }
    return render(request, 'portfolio/sobreWebsite.html', context)


def padroesUsados_view(request):
    padroesUsados = PadroesUsados.objects.all()
    context = {
        'padroesUsados': padroesUsados,
    }
    return render(request, 'portfolio/padroesUsados.html', context)
    
@login_required(login_url="/accounts/login")
def novaCadeira_view(request):

    form = CadeiraForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form}

    return render(request, 'portfolio/novaCadeira.html', context)

@login_required(login_url="/accounts/login")
def novoProjeto_view(request):

    form = ProjetoForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetosPessoais'))

    context = {'form': form}

    return render(request, 'portfolio/novoProjeto.html', context)

@login_required(login_url="/accounts/login")
def novoTfc_view(request):

    form = TfcsInteressantesForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:tfcsInteressantes'))
    context = {'form': form}

    return render(request, 'portfolio/novoTfc.html', context)



@login_required(login_url="/accounts/login")
def editarCadeira_view(request, cadeira_id):

    cadeira = CadeiraV2.objects.get(id=cadeira_id)
    form = CadeiraForm(request.POST or request.FILES or None, instance=cadeira)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form, 'cadeira_id': cadeira_id}
    return render(request, 'portfolio/editarCadeira.html', context)

@login_required(login_url="/accounts/login")
def editarTfc_view(request, tfc_id):
    tfc = TfcsInteressantes.objects.get(id=tfc_id)
    form = form = TfcsInteressantesForm(request.POST or request.FILES or None, instance=tfc)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:tfcsInteressantes'))
    
    
    context = {'form': form, 'tfc_id': tfc_id}
    return render(request, 'portfolio/editarTfc.html', context)

@login_required(login_url="/accounts/login")
def editarProjeto_view(request, projeto_id):

    projeto = Projeto.objects.get(id=projeto_id)
    form = ProjetoForm(request.POST or request.FILES or None, instance=projeto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetosPessoais'))

    context = {'form': form, 'projeto_id': projeto_id}
    return render(request, 'portfolio/editarProjeto.html', context)


@login_required(login_url="/accounts/login")
def apagarCadeira_view(request, cadeira_id):

    cadeira = CadeiraV2.objects.get(id=cadeira_id)
    cadeira.delete()
    return HttpResponseRedirect(reverse('portfolio:licenciatura'))


@login_required(login_url="/accounts/login")
def apagarTfc_view(request, tfc_id):

    tfc = TfcsInteressantes.objects.get(id=tfc_id)
    tfc.delete()
    return HttpResponseRedirect(reverse('portfolio:tfcsInteressantes'))


@login_required(login_url="/accounts/login")
def apagarProjeto_view(request, projeto_id):

    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return HttpResponseRedirect(reverse('portfolio:projetosPessoais'))

def pontuacao_quizz(request):
    score = 0
    if request.POST['p1'] == 'javascript':
        score += 1

    if request.POST['p2'] == 'Elementos_Semanticos':
        score += 1

    if request.POST['p3'] == 'TopRightBotLeft':
        score += 1

    if request.POST['p4'] == 'def_Function':
        score += 1

    if request.POST['p5'] == 'conf_url_view_html':
        score += 1

    return score

def desenha_grafico_resultados(request):
    pontuacoes = PontuacaoQuizz.objects.all().order_by('pontuacao')
    lista_nomes = []
    lista_pontuacao = []

    for person in pontuacoes:
        lista_nomes.append(person.nome)
        lista_pontuacao.append(person.pontuacao)

    plt.barh(lista_nomes, lista_pontuacao)
    plt.xlabel("Pontuações: ")
    plt.ylabel("Nomes: ")
    plt.savefig('portfolio/static/portfolio/images/graf.png', bbox_inches='tight')

    plt.autoscale()

    fig = plt.gcf()
    plt.close()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')

    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return uri

def quizz_view(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()

    context = {
        'data': desenha_grafico_resultados(request),
    }

    return render(request, 'portfolio/quizz.html', context)

