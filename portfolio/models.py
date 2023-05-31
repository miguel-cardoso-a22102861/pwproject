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
    


class Blog(models.Model):
    utilizador = models.OneToOneField(User, on_delete=models.CASCADE)
    github_link = models.URLField(max_length=200, blank=True)
    pythonanywhere_link = models.URLField(max_length=200, blank=True)

class Area(models.Model):
    nome = models.CharField(max_length=100)

class Autor(models.Model):
    utilizador = models.OneToOneField(User, on_delete=models.CASCADE)
    areasDeInteresse = models.ManyToManyField(Area)
    

class Post(models.Model):
    
    autor = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=25)
    descricao = models.TextField()
    link = models.CharField(max_length=100, blank=True)
    #imagem = models.ImageField(upload_to='images/', blank=True)

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    titulo = models.CharField(max_length=50)
    texto = models.TextField()

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    utilizador = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo
    

