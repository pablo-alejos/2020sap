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
    title = models.CharField(max_length=100, verbose_name="Nombre del capitulo",unique=True)
    bookTitle = models.CharField(max_length=100, verbose_name="Titulo del libro")
    bookEditorial = models.CharField(max_length=100, blank=True, verbose_name="Editorial del libro")
    bookIsbn = models.CharField(max_length=100, blank=True, verbose_name="ISBN del libro")
    publicationYear = models.CharField(max_length=4, verbose_name="Año de publicacion",default="")
    publicationMonth = models.CharField(max_length=12,verbose_name="Mes de publicación",blank=True,default="")
    file = models.FileField(blank=True, upload_to='archiving/', verbose_name="Capitulo de libro (PDF)")
    image = models.ImageField(blank=True,default='cover_images/default_cover.jpg', upload_to='cover_images',verbose_name="Cubierta o portada")
    status = (
        ( None, 'Selecciona estado'),
        ('En proceso','En proceso'), 
        ('Sometido','Sometido'), 
        ('Liberado','Liberado'), 
        )
    status =models.CharField(max_length=25,choices=status,verbose_name = "Estado",default="Sometido")
    #SystemFields
    timeStamp = models.DateTimeField(auto_now_add=True, verbose_name="Time Stamp")
    product = models.CharField(default="Capitulo", editable=False, max_length=15)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("bookChapter:bookChapter-detail", kwargs={"id": self.id})

    class Meta:
        verbose_name = 'Capitulo'