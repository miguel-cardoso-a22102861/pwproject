from django import forms
from django.forms import ModelForm

from .models import CadeiraV2, Pessoa, Post, Projeto, Tarefa, TfcsInteressantes


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

class CadeiraForm(ModelForm):
    class Meta:
        model = CadeiraV2
                
        fields = '__all__'

class TFCsInteressantesForm(forms.ModelForm):
    class Meta:
        model = TfcsInteressantes
        fields = '__all__'
                                                        

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


class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'


class TfcsInteressantesForm(ModelForm):
    class Meta:
        model = TfcsInteressantes
        fields = '__all__'

        


    


                                                                                       
    



    
