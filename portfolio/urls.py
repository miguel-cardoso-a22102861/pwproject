"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.urls import include, path
from . import views

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

app_name = 'portfolio'

urlpatterns = [
    path('', views.index_view),
    path('index', views.index_view),
    path('home', views.index_view, name='home'),
    # path('about', views.about_view, name='sobre'),
    path('home', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('laboratorios', views.laboratorios_view, name='laboratorios'),
    path('tarefas', views.tarefas_page_view, name='tarefas'),
    path('blog', views.blog_view, name='blog'),
    path('tarefasNova', views.tarefasNova_page_view, name='tarefasNova'),
    path('postNovo', views.postNovo_page_view, name='postNovo'),
    path('projetoPessoalNovo', views.projetosPessoaisNovo_view, name='projetosPessoaisNovo'),
    path('edita_tarefa/<int:tarefa_id>', views.edita_tarefa_view, name='edita'),
    path('apaga_tarefa/<int:tarefa_id>', views.apaga_tarefa_view, name='apaga'),
    path('post_edita/<int:post_id>', views.post_edita_view, name='postEdita'),
    path('post_apaga/<int:post_id>', views.post_apaga_view, name='postApaga'),
    path('tecnologiasUsadas', views.tecnologiasUsadas_view, name='tecnologiasUsadas'),
    path('tfcsInteresssantes', views.tfcsInteresssantes_view, name='tfcsInteressantes'),
    path('projetosPessoais', views.projetosPessoais_view, name='projetosPessoais'),
    path('pessoas', views.pessoas_view, name= 'pessoas'),
    path('aptidoesCompetencias', views.aptidoesCompetencias_view, name='aptidoesCompetencias'),
    path('cursos', views.licenciatura_view, name = 'cursos'),
    path('cadeira/<int:pk>/', views.cadeiraDetalhes_view, name='cadeiraDetail'),
    path('playground', views.playground_view, name = 'playground'),
    path('contactos', views.contactos_view, name = 'contactos'),
    path('educacao', views.educacao_view, name = 'educacao'),
    path('experienciaProfissional', views.experienciaProfissional_view, name = 'experienciaProfissional'),
    path('interesses', views.interesses_view, name='interesses'),
    path('projetosUniversidade', views.projetosUniversidade_view, name='projetosUniversidade'),
    path('tecnologiasExistentes', views.tecnologiasExistentes_view, name='tecnologiasExistentes'),
    path('noticiasPW', views.noticiasPW_view, name='noticiasPW'),
    path('sobreWebsite', views.sobreWebsite_view, name='sobreWebsite'),
    path('padroesUsados', views.padroesUsados_view, name='padroesUsados'),

    path('novaCadeira', views.novaCadeira_view, name='novaCadeira'),
    path('editarCadeira/<int:cadeira_id>/', views.editarCadeira_view, name='editarCadeira'),
    path('apagarCadeira/<int:cadeira_id>/', views.apagarCadeira_view, name='apagarCadeira'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)