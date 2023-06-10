from django import forms
from django.forms import ModelForm

from .models import Pessoa, Post, Projeto, Tarefa


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'



        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'descrição da tarefa'}),
            'prioridade': forms.NumberInput(attrs={'class': 'form-control', 'max': '3', 'min': '1'}),

        }

        labels = {
            'titulo': 'Título',
            'concluido': 'Concluído',
        }


        help_texts = {
            'prioridade': 'prioridade: baixa=1, media=2, alta=3',

        }

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Pessoa'}),
            'linkPaginaLusofona': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link da página da Lusofona'}),
            'linkLinkedIn': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link do LinkedIn'}),
            'linkAppPortfolio': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link da App Portfolio'}),
        }
        labels = {
            'nome': 'Nome',
            'linkPaginaLusofona': 'Link da página da Lusofona',
            'linkLinkedIn': 'Link do LinkedIn',
            'linkAppPortfolio': 'Link da App Portfolio',
        }
        help_texts = {
            'nome': 'Nome da Pessoa',
            'linkPaginaLusofona': 'Link da página da Lusofona',
        }
                                                         

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'autor'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'max': '3', 'min': '1'}),
        }

        labels = {
            'autor': 'Autor',
            'titulo': 'Título',
        }

        helps_texts = {
            'prioridade': 'prioridade: baixa=1, media=2, alta=3',
        }


class ProjetoPessoalForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título do projeto'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição do projeto'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'anoRealizacao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ano de realização'}),
            'participantes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Participantes'}),
            'linkGithub': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link do GitHub'}),
            'videoYoutube': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link do YouTube'}),
        }

        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'imagem': 'Imagem',
            'anoRealizacao': 'Ano de Realização',
            'participantes': 'Participantes',
            'linkGithub': 'Link do GitHub',
            'videoYoutube': 'Link do YouTube',
        }

        help_texts = {
            'titulo': 'Título do Projeto',
            'descricao': 'Descrição do Projeto',
            'imagem': 'Imagem do Projeto',
            'anoRealizacao': 'Ano de Realização do Projeto',
            'participantes': 'Participantes do Projeto',
            'linkGithub': 'Link do GitHub do Projeto',
            'videoYoutube': 'Link do YouTube do Projeto',
        }


                                                                                       
    



    
