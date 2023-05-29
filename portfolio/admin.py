from django.contrib import admin

from .models import Post, Tarefa
# Register your models here.
admin.site.register(Tarefa)

admin.site.register(Post)