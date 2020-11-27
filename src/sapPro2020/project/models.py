from django.db import models

from django.db import models
from django.contrib.admin.widgets import AdminDateWidget

from userSap.models import UserSap
from account.models import Account

class Project(models.Model):
    userResponsable = models.ForeignKey(
        UserSap, blank=True, on_delete=models.PROTECT, verbose_name="Responsable técnico")
    selectP = (
        (None, 'Selecciona estado'),
        ('Interno', 'Interno'),
        ('Externo', 'Externo'),
        ('Convenio', 'Convenio'),
        ('UABC', 'UABC'),
    )
    typeP = models.CharField(
        max_length=25, choices=selectP, verbose_name=" Tipo de proyecto")
    # El tipo lo haré que se automatice con el tiempo, para que desde la página decida el tipo de proyecto
    # y le aparezca un formulario que corresponda, de momento será genérico para que sea un mismo formulario
    # independientemente del tipo de proyecto
    title = models.CharField(max_length=100, verbose_name="Título de proyecto")
    announcement = models.CharField(
        blank=True, max_length=100, verbose_name=" Convocatoria (Si aplica)")
    amount = models.CharField(
        blank=True, max_length=50, verbose_name="Presupuesto (Si aplica)")
    participants = models.ManyToManyField(UserSap, blank=True, verbose_name="Participantes",related_name="authors")  
    code = models.CharField(verbose_name="Clave", blank=True, max_length=100)
    vigent = models.DateField(blank=True, verbose_name="Vigencia hasta")
    state = (
        (None, 'Selecciona estado'),
        ('Vigente', 'Vigente'),
        ('No vigente', 'No vigente'),
        ('Concluido', 'Concluido'),
    )
    status = models.CharField(
        blank=True, max_length=25, choices=state, verbose_name="Estado del proyecto")
    createdPubProject = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
