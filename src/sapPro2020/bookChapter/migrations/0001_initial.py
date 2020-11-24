# Generated by Django 3.1.3 on 2020-11-23 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
        ('account', '0001_initial'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nombre del capitulo')),
                ('bookTitle', models.CharField(max_length=100, verbose_name='Titulo del libro')),
                ('bookEditorial', models.CharField(blank=True, max_length=100, verbose_name='Editorial del libro')),
                ('bookIsbn', models.CharField(blank=True, max_length=100, verbose_name='ISBN del libro')),
                ('file', models.FileField(blank=True, upload_to='archiving/', verbose_name='Capitulo de libro (PDF)')),
                ('timeStamp', models.DateTimeField(auto_now_add=True, verbose_name='Time Stamp')),
                ('product', models.CharField(default='Capitulo', editable=False, max_length=15)),
                ('academyTribute', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='account.academy', verbose_name='Cuerpo académico educativo al que tributa')),
                ('authors', models.ManyToManyField(blank=True, to='author.Author', verbose_name='Otros Autores')),
                ('eventPublication', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='event.event', verbose_name='Evento en el que fue publicado')),
                ('programTribute', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='account.program', verbose_name='Programa educativo al que tributa')),
            ],
        ),
    ]