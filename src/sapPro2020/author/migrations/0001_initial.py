# Generated by Django 3.1.3 on 2020-11-23 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=50, verbose_name='Nombre(s)')),
                ('lastNameA', models.CharField(blank=True, max_length=50, verbose_name='Apellido Paterno')),
                ('lastNameB', models.CharField(blank=True, max_length=50, verbose_name='Apellido Materno')),
                ('timeStamp', models.DateTimeField(auto_now_add=True, verbose_name='Time Stamp')),
            ],
        ),
    ]
