# Generated by Django 3.1.3 on 2021-01-06 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20210105_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Título de proyecto'),
        ),
    ]