# Generated by Django 3.1.3 on 2021-01-06 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userSap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='numEmp',
            field=models.CharField(blank=True, max_length=20, verbose_name='Numero de empleado'),
        ),
    ]
