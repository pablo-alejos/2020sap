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
            name='BookChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nombre del capitulo')),
                ('bookTitle', models.CharField(max_length=100, verbose_name='Titulo del libro')),
                ('bookEditorial', models.CharField(blank=True, max_length=100, verbose_name='Editorial del libro')),
                ('bookIsbn', models.CharField(blank=True, max_length=100, verbose_name='ISBN del libro')),
                ('publicationYear', models.CharField(default='', max_length=4, verbose_name='Año de publicacion')),
                ('publicationMonth', models.CharField(blank=True, default='', max_length=12, verbose_name='Mes de publicación')),
                ('file', models.FileField(blank=True, upload_to='archiving/', verbose_name='Capitulo de libro (PDF)')),
                ('image', models.ImageField(blank=True, default='cover_images/default_cover.jpg', upload_to='cover_images', verbose_name='Cubierta o portada')),
                ('status', models.CharField(choices=[(None, 'Selecciona estado'), ('En proceso', 'En proceso'), ('Sometido', 'Sometido'), ('Liberado', 'Liberado')], default='Sometido', max_length=25, verbose_name='Estado')),
                ('timeStamp', models.DateTimeField(auto_now_add=True, verbose_name='Time Stamp')),
                ('product', models.CharField(default='Capitulo', editable=False, max_length=15)),
                ('academyTribute', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='account.academy', verbose_name='Cuerpo académico educativo al que tributa')),
                ('authors', models.ManyToManyField(blank=True, to='author.Author', verbose_name='Otros Autores')),
                ('eventPublication', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='event.event', verbose_name='Evento en el que fue publicado')),
                ('programTribute', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='account.program', verbose_name='Programa educativo al que tributa')),
            ],
        ),
    ]
