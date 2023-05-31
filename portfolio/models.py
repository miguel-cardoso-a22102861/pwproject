from collections import UserDict
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length= 100)
    prioridade = models.IntegerField(default=1)
    concluido = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class BlogOwner(models.Model):
    nome = models.TextField(max_length= 25)
    github_link = models.URLField(max_length=200, blank=True)
    pythonanywhere_link = models.URLField(max_length=200, blank=True)

class Area(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=25)
    areasDeInteresse = models.ManyToManyField(Area, related_name='autores')

    
    def __str__(self):
        return self.nome
    

class Post(models.Model):

    autores = models.ManyToManyField(Autor, related_name='posts')
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=25)
    descricao = models.TextField()
    link = models.CharField(max_length=100, blank=True)
    imagem = models.ImageField(upload_to='images/', blank=True)
    comentarios = models.ManyToManyField('Comentario', related_name='posts')
    like = models.IntegerField(default=0)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.titulo


class Blog(models.Model):
    utilizador = models.OneToOneField(BlogOwner, on_delete=models.CASCADE, unique=True)
    areas = models.ManyToManyField(Area, related_name='blogs')

class Comentario(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()

    def __str__(self):
        return self.titulo



    

