from django.db import models

from django.urls import reverse
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget

from userSap.models import UserSap
from account.models import Account


class Project(models.Model):
    userResponsable = models.ForeignKey(UserSap,
                                        on_delete=models.PROTECT,
                                        verbose_name="Responsable técnico")
    selectP = (
        (None, 'Selecciona estado'),
        ('Interno', 'Interno'),
        ('Externo', 'Externo'),
        ('Convenio', 'Convenio'),
        ('UABC', 'UABC'),
    )
    typeP = models.CharField(max_length=25,
                             choices=selectP,
                             verbose_name=" Tipo de proyecto")
    title = models.CharField(max_length=100, verbose_name="Título de proyecto")
    announcement = models.CharField(blank=True,
                                    max_length=100,
                                    verbose_name=" Convocatoria (Si aplica)")
    amount = models.CharField(blank=True,
                              max_length=50,
                              verbose_name="Presupuesto (Si aplica)")
    participants = models.ManyToManyField(UserSap,
                                          blank=True,
                                          verbose_name="Participantes",
                                          related_name="authors")
    code = models.CharField(verbose_name="Clave", unique=True, max_length=100)
    vigent = models.DateField(verbose_name="Vigencia hasta")
    state = (
        (None, 'Selecciona estado'),
        ('Vigente', 'Vigente'),
        ('No vigente', 'No vigente'),
        ('Concluido', 'Concluido'),
    )
    status = models.CharField(max_length=25,
                              choices=state,
                              verbose_name="Estado del proyecto",
                              default="Vigente")
    createdPubProject = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project:project-detail", kwargs={"id": self.id})


    class Meta:
        verbose_name = 'Proyecto'