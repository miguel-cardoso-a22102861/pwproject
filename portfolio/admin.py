from django.contrib import admin

from .models import CadeiraV2, Educacao, PadroesUsados, ProfessorV2, Projeto, AptidoesCompetencias, Area, Autor, Blog, BlogOwner, Cadeira, Comentario, Contacto, Curso, CursoModelo, Formacao, Interesses, LaboratoriosPW, LinkRepos, NoticiasPW, Pessoa, Post, Rodape, Tarefa, TecnologiasExistentesPW, TecnologiasPW, TfcsInteressantes,TipoCompetencias,SobreWebsite

# Register your models here.
admin.site.register(Tarefa)

admin.site.register(Post)
admin.site.register(Area)
admin.site.register(Autor)
admin.site.register(Blog)
admin.site.register(Comentario)
admin.site.register(BlogOwner)
admin.site.register(Cadeira)
admin.site.register(CursoModelo)
admin.site.register(Curso)
admin.site.register(Formacao)
admin.site.register(Pessoa)
admin.site.register(Projeto)
admin.site.register(TipoCompetencias)
admin.site.register(Interesses)
admin.site.register(AptidoesCompetencias)
admin.site.register(TecnologiasPW)
admin.site.register(LinkRepos)
admin.site.register(LaboratoriosPW)
admin.site.register(NoticiasPW)
admin.site.register(SobreWebsite)
admin.site.register(Contacto)
admin.site.register(Rodape)
admin.site.register(Educacao)
admin.site.register(TfcsInteressantes)
admin.site.register(PadroesUsados)
admin.site.register(TecnologiasExistentesPW)
admin.site.register(ProfessorV2)
admin.site.register(CadeiraV2)



