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


class Curso(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    carga_horaria = models.IntegerField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.nome
    

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    linkPaginaLusofona = models.URLField(max_length=200, blank=True)
    linkLinkedIn = models.URLField(max_length=200, blank=True)
    linkAppPortfolio = models.URLField(blank=True)

    def __str__(self):
        return self.nome
    
class TipoCompetencias(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=100)

class Projeto(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)
    imagem = models.ImageField(upload_to='images/', blank=True)
    anoRealizacao = models.IntegerField()
    participantes = models.ManyToManyField(Pessoa, related_name='trabalhos')
    linkGithub = models.URLField(max_length=120, blank=True)
    videoYoutube = models.URLField(blank=True)

    def __str__(self):
        return self.titulo


class Cadeira(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=100)
    semestre = models.IntegerField()
    ects = models.IntegerField()
    anoLetivo = models.IntegerField()
    professores = models.ManyToManyField(Autor, related_name='cadeiras')
    projetosRealizados = models.ManyToManyField(Projeto, related_name='cadeiras')
   
class AptidoesCompetencias(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=100)
    listaProjetos = models.ManyToManyField(Projeto, related_name='aptidoesCompetencias')
    listaDisciplinas = models.ManyToManyField(Cadeira, related_name='aptidoesCompetencias')




    def __str__(self):
        return self.nome

class CursoModelo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    cadeiras = models.ManyToManyField(Cadeira, related_name='cursos')


    def __str__(self):
        return self.nome
class Formacao(models.Model):
    curso = models.ForeignKey(CursoModelo, on_delete=models.CASCADE, related_name='formacoes')
    local = models.CharField(max_length=50)
    imagemLogotipo = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.curso


class Interesses(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=100)
    fotografia = models.ImageField(upload_to='images/', blank=True)
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.titulo
    

class Tfcs(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    orientador = models.ManyToManyField(Pessoa)
    anoDeRealizacao = models.IntegerField()
    imagem = models.ImageField(default='default.png', blank=True)
    resumo = models.CharField(max_length= 1000)
    linkRelatorio = models.URLField(blank= False)
    linkGithub = models.URLField(blank= True)
    linkVideoYt = models.URLField(blank=True)


class TecnologiasPW(models.Model):
    nome = models.CharField(max_length= 500)
    anoDeCriacao = models.IntegerField()
    criador = models.ManyToManyField(Pessoa, related_name='tecnologias', blank=True)
    logotipo = models.ImageField(upload_to='images/',blank=True)
    siteOficial = models.URLField(blank= False)
    linguagens = models.CharField(max_length= 500)
    descricao = models.CharField(max_length=750)

class LinkRepos(models.Model):
    titulo = models.CharField(max_length=50)
    linkGithub = models.URLField(blank=False)

    def __str__(self):
        return self.titulo
    

class LaboratoriosPW(models.Model):
    linksRepos = models.ManyToManyField(LinkRepos, blank=False)
    titulo = models.CharField(max_length= 50, blank= False)
    descricaoTopicos = models.CharField(max_length= 500)


    def __str__(self):
        return self.titulo
    
class NoticiasPW(models.Model):
    titulo = models.CharField(max_length= 50, blank= False)
    descricaoNoticia = models.CharField(max_length= 400, blank=False)
    imagemNoticia = models.ImageField(upload_to='images/')
    linkNoticia = models.URLField(blank= False)

    def __str__(self):
        return self.titulo


class sobreEsteWS(models.Model):
    mapaDoSite = models.ImageField(upload_to='images/', blank=False)
    descricaoBD = models.CharField(max_length= 244)
    listaTecnologiasUsadas = models.ManyToManyField(TecnologiasPW, blank=False)
    listaPadroesUsados = models.CharField(max_length= 255)
    comentarios = models.ManyToManyField(Comentario, max_length=10)


    def __str__(self):
        return self.descricaoBD
    

class Contacto(models.Model):
    linkLinkedin = models.URLField(blank=False)
    linkGithub = models.URLField(blank=False)
    nomeCidade = models.CharField(blank=False, max_length=255)
    linkFacebook = models.URLField(blank= True)



class Rodape(models.Model):
    linkGithub = models.URLField(blank=False)
    linkRepo = models.OneToOneField(LinkRepos, blank=False , on_delete=models.CASCADE, related_name='rodape')
    pythonAnywhere = models.URLField(blank=False)
    
    




    











    






