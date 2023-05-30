from django import forms
from django.forms import ModelForm

from .models import Post, Tarefa


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

    
