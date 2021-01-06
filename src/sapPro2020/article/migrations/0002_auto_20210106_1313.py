# Generated by Django 3.1.3 on 2021-01-06 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
        ('article', '0001_initial'),
        ('userSap', '0001_initial'),
        ('author', '0001_initial'),
        ('tag', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='academyTribute',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='userSap.academy', verbose_name='Cuerpo académico educativo al que tributa'),
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(blank=True, to='author.Author', verbose_name='Otros Autores'),
        ),
        migrations.AddField(
            model_name='article',
            name='eventPublication',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='event.event', verbose_name='Evento en el que fue publicado'),
        ),
        migrations.AddField(
            model_name='article',
            name='journal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='article.journal', verbose_name='Nombre de revista'),
        ),
        migrations.AddField(
            model_name='article',
            name='programTribute',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='userSap.program', verbose_name='Programa educativo al que tributa'),
        ),
        migrations.AddField(
            model_name='article',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.project', verbose_name='Proyecto'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tag.Tag', verbose_name='Etiquetas'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Autor principal'),
        ),
    ]
