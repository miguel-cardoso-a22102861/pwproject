# Generated by Django 4.2.1 on 2023-06-07 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_rename_tfc_tfcs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aptidoescompetencias',
            name='descricao',
            field=models.TextField(max_length=700),
        ),
    ]
