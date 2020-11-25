# Generated by Django 3.1.3 on 2020-11-25 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('event', '0001_initial'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la revista')),
                ('editorial', models.CharField(max_length=50, verbose_name='Editorial')),
                ('country', models.CharField(max_length=50, verbose_name='País')),
                ('quartMagazine', models.CharField(choices=[(None, 'Selecciona estado'), (' q1 ', ' q1 '), (' q2 ', ' q2 '), (' q3 ', ' q3 '), (' q4 ', ' q4 ')], max_length=25, verbose_name='Cuartiles')),
                ('referenceMagazine', models.CharField(max_length=100, verbose_name='Enlace a revista (opcional)')),
                ('issn', models.CharField(max_length=30, verbose_name='ISSN')),
                ('timeStamp', models.DateTimeField(auto_now_add=True, verbose_name='Time Stamp')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Título de artículo')),
                ('indexed', models.BooleanField(default=False, verbose_name='Indizado')),
                ('indexInfo', models.CharField(max_length=220, verbose_name='Índice en que se encuentra')),
                ('arbitration', models.BooleanField(default=False, verbose_name='Arbitraje')),
                ('month', models.CharField(max_length=2, verbose_name='Mes de publicacion')),
                ('year', models.CharField(max_length=4, verbose_name='Año de publicacion')),
                ('pages', models.CharField(max_length=50, verbose_name='Páginas donde está publicado')),
                ('status', models.CharField(choices=[(None, 'Selecciona estado'), ('En proceso', 'En proceso'), ('Sometido', 'Sometido'), ('Liberado', 'Liberado')], max_length=25, verbose_name='Estado')),
                ('file', models.FileField(blank=True, upload_to='archiving/', verbose_name='Archivo (PDF)')),
                ('image', models.ImageField(blank=True, default='cover_images/default_cover.jpg', upload_to='cover_images', verbose_name='Cubierta o portada')),
                ('timeStamp', models.DateTimeField(auto_now_add=True, verbose_name='Time Stamp')),
                ('product', models.CharField(default='Articulo', editable=False, max_length=15)),
                ('academyTribute', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='account.academy', verbose_name='Cuerpo académico educativo al que tributa')),
                ('authors', models.ManyToManyField(blank=True, to='author.Author', verbose_name='Otros Autores')),
                ('eventPublication', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='event.event', verbose_name='Evento en el que fue publicado')),
                ('journal', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='article.journal', verbose_name='Nombre de revista')),
                ('programTribute', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='account.program', verbose_name='Programa educativo al que tributa')),
            ],
        ),
    ]
