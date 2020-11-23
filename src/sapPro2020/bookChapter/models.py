from django.db import models
from django.urls import reverse

from userSap.models import UserSap
from project.models import Project
from account.models import Account, Academy,Program
from tag.models import Tag
from event.models import Event
from author.models import Author


class BookChapter(models.Model):
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
    title = models.CharField(max_length=100, verbose_name="Nombre del capitulo")
    bookTitle = models.CharField(max_length=100, verbose_name="Titulo del libro")
    bookEditorial = models.CharField(max_length=100, blank=True, verbose_name="Editorial del libro")
    bookIsbn = models.CharField(max_length=100, blank=True, verbose_name="ISBN del libro")
    file = models.FileField(blank=True, upload_to='archiving/', verbose_name="Capitulo de libro (PDF)")
    #SystemFields
    timeStamp = models.DateTimeField(auto_now_add=True, verbose_name="Time Stamp")
    product = models.CharField(default="Capitulo", editable=False, max_length=15)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("bookChapter:bookChapter-detail", kwargs={"id": self.id})