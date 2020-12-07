from django.db import models

from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de la etiqueta")
    tag = models.CharField(max_length=10, verbose_name="Tipo")
    timeStamp = models.DateTimeField(auto_now_add=True, verbose_name="Time Stamp")

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("tag:tag-detail", kwargs={"id": self.id})

    class Meta:
        verbose_name = 'Etiqueta'
        