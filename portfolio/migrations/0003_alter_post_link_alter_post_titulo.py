# Generated by Django 4.2.1 on 2023-05-30 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=25),
        ),
    ]
