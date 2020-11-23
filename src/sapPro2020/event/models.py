from django.db import models
from django.urls import reverse



class Event(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del evento", blank=True)
    eventCreated = models.CharField(max_length=100, verbose_name="Fecha de creacion del evento", blank=True)
    topic = models.CharField(max_length=100, verbose_name="Tema", blank=True)
    headquarters = models.CharField(max_length=100, verbose_name="Sede", blank=True)
    address = models.CharField(max_length=100, verbose_name="Dirección", blank=True)
    eventSelect = (
        (None, 'Seleccionar tipo'),
        ('Congreso', 'Congreso'),
        ('Foro', 'Foro'),
        ('Simposio', 'Simposio'),
    )
    event = models.CharField(max_length=100,choices=eventSelect, verbose_name="Tipo", blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True, verbose_name="Time Stamp")

    def __str__(self):
        return f"{self.event} {'-'} {self.name}"



class Forum(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Foro", blank=True)

    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha")

    eventCreated = models.CharField(
        max_length=100, verbose_name="Fecha de creacion del evento", blank=True)

    topic = models.CharField(
        max_length=100, verbose_name="Tema", blank=True)

    headquarters = models.CharField(
        max_length=100, verbose_name="Sede", blank=True)

    address = models.CharField(
        max_length=100, verbose_name="Dirección", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("forum:forum-detail", kwargs={"id": self.id})


class Symposium(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Nombre del evento", blank=True)

    topic = models.CharField(
        max_length=100, verbose_name="Tema", blank=True)

    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha")

    eventCreated = models.CharField(
        max_length=100, verbose_name="Fecha de creacion del evento", blank=True)

    headquarters = models.CharField(
        max_length=100, verbose_name="Sede", blank=True)

    address = models.CharField(
        max_length=100, verbose_name="Dirección", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("symposium:symposium-detail", kwargs={"id": self.id})


class Congress(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Congreso", blank=True)

    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha")

    eventCreated = models.CharField(
        max_length=100, verbose_name="Fecha de creacion del evento", blank=True)

    topic = models.CharField(
        max_length=100, verbose_name="Tema", blank=True)

    headquarters = models.CharField(
        max_length=100, verbose_name="Sede", blank=True)

    address = models.CharField(
        max_length=100, verbose_name="Dirección", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("congress:congress-detail", kwargs={"id": self.id})
