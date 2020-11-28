# Generated by Django 3.1.3 on 2020-11-28 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20201127_0542'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academy',
            options={'verbose_name': 'Comite academico'},
        ),
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Cuenta'},
        ),
        migrations.AlterModelOptions(
            name='program',
            options={'verbose_name': 'Programa educativo'},
        ),
        migrations.AlterField(
            model_name='academy',
            name='name',
            field=models.CharField(blank=True, max_length=150, unique=True, verbose_name='Cuerpo académico'),
        ),
        migrations.AlterField(
            model_name='account',
            name='numEmp',
            field=models.CharField(blank=True, max_length=20, unique=True, verbose_name='Numero de empleado'),
        ),
        migrations.AlterField(
            model_name='program',
            name='name',
            field=models.CharField(blank=True, max_length=150, unique=True, verbose_name='Nombre del programa'),
        ),
    ]
