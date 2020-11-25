from django.db import models
from django.urls import reverse
from django.core.validators import ValidationError 
from userSap.models import UserSap 
from project.models import Project
from account.models import Account, Program, Academy
from event.models import Event
from tag.models import Tag
from author.models import Author



class Journal(models.Model):
    name = models.CharField(max_length = 100,verbose_name = "Nombre de la revista")  
    editorial = models.CharField(max_length = 50,verbose_name = "Editorial")
    country = models.CharField(max_length = 50,verbose_name = "País")  
    quartile = (
        ( None, 'Selecciona estado'),
        (' q1 ',' q1 '), 
        (' q2 ',' q2 '), 
        (' q3 ',' q3 '), 
        (' q4 ',' q4 '),  
        )
    quartMagazine = models.CharField(max_length=25,choices=quartile,verbose_name = "Cuartiles")
    referenceMagazine = models.CharField(max_length=100,verbose_name = "Enlace a revista (opcional)")
    issn = models.CharField(max_length = 30, verbose_name = "ISSN")
    timeStamp = models.DateTimeField(auto_now_add=True, verbose_name="Time Stamp")

    def __str__(self):
        return f'{self.name} - {self.quartMagazine}' 



class Article(models.Model):      
    #ForeignKeys
    project = models.ForeignKey(Project, on_delete=models.PROTECT,verbose_name = "Proyecto")
    journal = models.ForeignKey(Journal, on_delete=models.PROTECT,verbose_name = "Nombre de revista", blank=True)
    user = models.ForeignKey(UserSap, on_delete=models.PROTECT,verbose_name = "Autor principal")
    programTribute = models.ForeignKey(Program, on_delete=models.PROTECT, verbose_name="Programa educativo al que tributa",blank=True,default="")
    academyTribute = models.ForeignKey(Academy, on_delete=models.PROTECT, verbose_name="Cuerpo académico educativo al que tributa",blank=True,default="")
    eventPublication = models.ForeignKey(Event, on_delete=models.PROTECT, verbose_name="Evento en el que fue publicado",blank=True,default="")
    #ManyToManyFields
    authors = models.ManyToManyField(Author,blank=True,verbose_name = "Otros Autores")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Etiquetas")
    #Fields
    title = models.CharField(max_length = 50,verbose_name = "Título de artículo")
    indexed = models.BooleanField(default=False,verbose_name = "Indizado")
    indexInfo = models.CharField(max_length = 220,verbose_name = "Índice en que se encuentra")
    arbitration = models.BooleanField(default=False,verbose_name = "Arbitraje")
    month = models.CharField(max_length=2,verbose_name = "Mes de publicacion")
    year = models.CharField(max_length=4,verbose_name = "Año de publicacion")
    pages = models.CharField(max_length = 50,verbose_name = "Páginas donde está publicado")
    status = (
        ( None, 'Selecciona estado'),
        ('En proceso','En proceso'), 
        ('Sometido','Sometido'), 
        ('Liberado','Liberado'), 
        )
    status =models.CharField(max_length=25,choices=status,verbose_name = "Estado")
    file = models.FileField(blank=True, upload_to='archiving/',verbose_name="Archivo (PDF)")
    image = models.ImageField(blank=True,default='cover_images/default_cover.jpg', upload_to='cover_images',verbose_name="Cubierta o portada")
    #SystemFields
    timeStamp = models.DateTimeField(auto_now_add=True, verbose_name="Time Stamp")
    product = models.CharField(default="Articulo",editable=False,max_length=15)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article:article-detail",kwargs={"id":self.id})
