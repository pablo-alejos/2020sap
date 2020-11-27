from django.db import models
from django.urls import reverse
from author.models import Author

class Academy(models.Model):
    name = models.CharField(max_length=150, verbose_name="Cuerpo académico", blank=True,unique=True)
    timeStamp = models.DateTimeField(auto_now_add=True, verbose_name="Time Stamp")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("account:academy-detail",kwargs={"id": self.id})

    class Meta:
        verbose_name = 'Comite academico'

class Program(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre del programa", blank=True,unique=True)
    key = models.CharField(max_length=150, verbose_name="Clave del programa", blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True, verbose_name="Time Stamp")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("account:program-detail", kwargs={"id": self.id})

    class Meta:
        verbose_name = 'Programa educativo'

class Account(models.Model):
    program = models.ForeignKey(Program, on_delete=models.PROTECT, verbose_name="Programa educativo", blank=True, null=True)
    academy = models.ForeignKey(Academy, on_delete=models.PROTECT, verbose_name="Cuerpo académico", blank=True, null=True)
    numEmp = models.CharField(max_length=20, verbose_name="Numero de empleado", blank=True)
    firstName = models.CharField(max_length=50, verbose_name="Nombre(s)", blank=True)
    lastNameA = models.CharField(max_length=50, verbose_name="Apellido Paterno", blank=True)
    lastNameB = models.CharField(max_length=50, verbose_name="Apellido Materno", blank=True)
    author_info = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Define esta cuenta con un registro en la tabla de autores",null=True)
    timeStamp = models.DateTimeField(auto_now_add=True, verbose_name="Time Stamp")
    

    def __str__(self):
        return f'{self.firstName} {self.lastNameA} {self.lastNameB}'

    def get_absolute_url(self):
        return reverse("account:account-detail", kwargs={"id": self.id})

    class Meta:
        verbose_name = 'Cuenta'