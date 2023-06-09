# Generated by Django 4.2.1 on 2023-06-08 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_rename_tfcs_tfcsinteresssantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='TecnologiasExistentesPW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500)),
                ('anoDeCriacao', models.IntegerField()),
                ('logotipo', models.ImageField(blank=True, upload_to='images/')),
                ('siteOficial', models.URLField()),
                ('linguagens', models.CharField(max_length=500)),
                ('descricao', models.CharField(max_length=750)),
                ('criador', models.ManyToManyField(blank=True, related_name='tecnologiasExistentes', to='portfolio.pessoa')),
            ],
        ),
    ]
