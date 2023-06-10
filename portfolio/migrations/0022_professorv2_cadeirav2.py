# Generated by Django 4.2.1 on 2023-06-10 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_alter_tecnologiasexistentespw_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessorV2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='CadeiraV2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=55)),
                ('descricao', models.TextField(max_length=300)),
                ('ects', models.FloatField(default=5.0)),
                ('ranking', models.IntegerField(default=4)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.professorv2')),
            ],
        ),
    ]