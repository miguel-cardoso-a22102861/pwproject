from django.contrib import admin

from .models import Area, Autor, Blog, BlogOwner, Comentario, Post, Tarefa
# Register your models here.
admin.site.register(Tarefa)

admin.site.register(Post)
admin.site.register(Area)
admin.site.register(Autor)
admin.site.register(Blog)
admin.site.register(Comentario)
admin.site.register(BlogOwner)
