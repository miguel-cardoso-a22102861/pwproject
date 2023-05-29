from django.db import models

# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length= 100)
    prioridade = models.IntegerField(default=1)
    concluido = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    


class Post(models.Model):
    autor = models.CharField(max_length= 100)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length= 100)
    descricao = models.TextField()
    link = models.CharField(max_length= 100)



    def __str__(self):
        return self.titulo
    

