# Generated by Django 3.1.3 on 2020-12-11 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0003_auto_20201128_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='code',
            field=models.CharField(max_length=100, unique=True, verbose_name='Clave'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[(None, 'Selecciona estado'), ('Vigente', 'Vigente'), ('No vigente', 'No vigente'), ('Concluido', 'Concluido')], default='Vigente', max_length=25, verbose_name='Estado del proyecto'),
        ),
        migrations.AlterField(
            model_name='project',
            name='userResponsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Responsable técnico'),
        ),
        migrations.AlterField(
            model_name='project',
            name='vigent',
            field=models.DateField(verbose_name='Vigencia hasta'),
        ),
    ]