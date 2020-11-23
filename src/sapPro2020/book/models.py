from django.db import models

from django.urls import reverse

from userSap.models import UserSap
from project.models import Project
from account.models import Account, Academy,Program
from tag.models import Tag
from event.models import Event
from author.models import Author



class Book(models.Model):
    #ForeignKeys
    project = models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name="Proyecto")
    user = models.ForeignKey(UserSap, on_delete=models.PROTECT, verbose_name="Autor principal")
    programTribute = models.ForeignKey(Program, on_delete=models.PROTECT, verbose_name="Programa educativo al que tributa",blank=True,default="")
    academyTribute = models.ForeignKey(Academy, on_delete=models.PROTECT, verbose_name="Cuerpo académico educativo al que tributa",blank=True,default="")
    eventPublication = models.ForeignKey(Event, on_delete=models.PROTECT, verbose_name="Evento en el que fue publicado",blank=True,default="")
    #ManyToManyFields    
    authors = models.ManyToManyField(Author,blank=True,verbose_name = "Otros Autores")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Etiquetas")
    #Fields 
    title = models.CharField(max_length=220, verbose_name="Titulo del libro")
    editorial = models.CharField(max_length=220, verbose_name="Editorial",blank=True)
    isbn = models.CharField(max_length=17, verbose_name="ISBN")
    publicationYear = models.CharField(max_length=4, verbose_name="Año de publicacion")
    file = models.FileField(upload_to="archiving/", verbose_name="Libro (PDF)")
    status = (
        ( None, 'Selecciona estado'),
        ('En proceso','En proceso'), 
        ('Sometido','Sometido'), 
        ('Liberado','Liberado'), 
        )
    status =models.CharField(max_length=25,choices=status,verbose_name = "Estado")
    #SystemFields
    timeStamp = models.DateTimeField(auto_now_add=True, verbose_name="Time Stamp")
    product = models.CharField(default="Libro", editable=False, max_length=15)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book:book-detail", kwargs={"id": self.id})