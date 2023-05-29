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
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index_view),
    path('index', views.index_view),
    path('home', views.index_view, name='home'),
    # path('about', views.about_view, name='sobre'),
    path('home', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('tarefas', views.tarefas_page_view, name='tarefas'),
    path('blog', views.blog_view, name='blog'),
    path('tarefasNova', views.tarefasNova_page_view, name='tarefasNova'),
    path('blogNovo', views.postNovo_page_view, name='postNovo'),
    path('edita_tarefa/<int:tarefa_id>', views.edita_tarefa_view, name='edita'),
    path('apaga_tarefa/<int:tarefa_id>', views.apaga_tarefa_view, name='apaga'),
    
    
]