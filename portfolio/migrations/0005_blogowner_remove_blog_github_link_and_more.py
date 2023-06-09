# Generated by Django 4.2.1 on 2023-05-31 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_area_like_comentario_blog_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(max_length=25)),
                ('github_link', models.URLField(blank=True)),
                ('pythonanywhere_link', models.URLField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='github_link',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='pythonanywhere_link',
        ),
        migrations.AddField(
            model_name='area',
            name='posts',
            field=models.ManyToManyField(related_name='area', to='portfolio.post'),
        ),
        migrations.AddField(
            model_name='blog',
            name='areas',
            field=models.ManyToManyField(to='portfolio.area'),
        ),
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='blog',
            name='utilizador',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portfolio.blogowner'),
        ),
    ]
