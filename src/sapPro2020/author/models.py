from os import name
from django.db import models
from django.urls import reverse

class Author(models.Model):
    firstName = models.CharField(max_length=50, verbose_name="Nombre(s)")
    lastNameA = models.CharField(max_length=50, verbose_name="Apellido Paterno")
    lastNameB = models.CharField(max_length=50, verbose_name="Apellido Materno")
    timeStamp = models.DateTimeField(auto_now_add=True, verbose_name="Time Stamp")

    def __str__(self):
        return f'{self.firstName} {self.lastNameA} {self.lastNameB}'

    def get_absolute_url(self):
        return reverse("author:author-detail", kwargs={"id": self.id})

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'