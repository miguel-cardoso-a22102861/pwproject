# Generated by Django 4.2.1 on 2023-06-14 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0023_rename_tfcsinteresssantes_tfcsinteressantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontuacaoQuizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('pontuacao', models.IntegerField(default=0)),
            ],
        ),
    ]