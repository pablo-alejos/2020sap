from django.db import models
from django.urls import reverse



class Event(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del evento")
    eventStart = models.CharField(max_length=100, verbose_name="Fecha de inicio del evento")
    eventFinish = models.CharField(max_length=100, verbose_name="Fecha de finalización del evento")
    topic = models.CharField(max_length=100, verbose_name="Tema")
    headquarters = models.CharField(max_length=100, verbose_name="Sede")
    address = models.CharField(max_length=100, verbose_name="Dirección")
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

    class Meta:
        verbose_name = 'Evento'