# Generated by Django 4.2.1 on 2023-06-08 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_alter_aptidoescompetencias_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('imagem', models.ImageField(blank=True, upload_to='images/')),
                ('descricao', models.CharField(max_length=700)),
            ],
        ),
    ]
