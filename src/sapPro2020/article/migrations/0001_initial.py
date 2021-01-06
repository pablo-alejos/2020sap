# Generated by Django 3.1.3 on 2021-01-06 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220, unique=True, verbose_name='Título de artículo')),
                ('indexed', models.BooleanField(blank=True, default=False, null=True, verbose_name='Indizado')),
                ('indexInfo', models.CharField(blank=True, max_length=220, null=True, verbose_name='Índice en que se encuentra')),
                ('arbitration', models.BooleanField(blank=True, default=False, null=True, verbose_name='Arbitraje')),
                ('month', models.CharField(max_length=2, verbose_name='Mes de publicacion')),
                ('publicationYear', models.CharField(max_length=4, verbose_name='Año de publicacion')),
                ('pages', models.CharField(max_length=50, verbose_name='Páginas donde está publicado')),
                ('status', models.CharField(choices=[(None, 'Selecciona estado'), ('En proceso', 'En proceso'), ('Sometido', 'Sometido'), ('Liberado', 'Liberado')], default='Sometido', max_length=25, verbose_name='Estado')),
                ('file', models.FileField(unique=True, upload_to='archiving/', verbose_name='Articulo (PDF)')),
                ('image', models.ImageField(blank=True, default='cover_images/default_cover.jpg', upload_to='cover_images', verbose_name='Cubierta o portada')),
                ('timeStamp', models.DateTimeField(auto_now_add=True, verbose_name='Time Stamp')),
                ('product', models.CharField(default='Articulo', editable=False, max_length=15)),
            ],
            options={
                'verbose_name': 'Articulo',
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre de la revista')),
                ('editorial', models.CharField(max_length=50, verbose_name='Editorial')),
                ('country', models.CharField(max_length=50, verbose_name='País')),
                ('quartMagazine', models.CharField(choices=[(None, 'Selecciona cuartiles'), (' q1 ', ' q1 '), (' q2 ', ' q2 '), (' q3 ', ' q3 '), (' q4 ', ' q4 ')], max_length=25, verbose_name='Cuartiles')),
                ('referenceMagazine', models.CharField(blank=True, max_length=100, verbose_name='Enlace a revista')),
                ('issn', models.CharField(max_length=30, unique=True, verbose_name='ISSN')),
                ('timeStamp', models.DateTimeField(auto_now_add=True, verbose_name='Time Stamp')),
            ],
            options={
                'verbose_name': 'Revista',
            },
        ),
    ]
