from django.db import models
from django.urls import reverse, reverse_lazy

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from django.db.models.signals import post_save
from django.dispatch import receiver

from .managers import UserSapManager
from author.models import Author


class Academy(models.Model):
    name = models.CharField(max_length=150,
                            verbose_name="Cuerpo académico",
                            blank=True,
                            unique=True)
    timeStamp = models.DateTimeField(auto_now_add=True,
                                     verbose_name="Time Stamp")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("userSap:academy-detail", kwargs={"id": self.id})

    class Meta:
        verbose_name = 'Comite academico'


class Program(models.Model):
    name = models.CharField(max_length=150,
                            verbose_name="Nombre del programa",
                            blank=True,
                            unique=True)
    key = models.CharField(max_length=150,
                           verbose_name="Clave del programa",
                           blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True,
                                     verbose_name="Time Stamp")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("userSap:program-detail", kwargs={"id": self.id})

    class Meta:
        verbose_name = 'Programa educativo'


class Account(models.Model):
    program = models.ForeignKey(Program,
                                on_delete=models.PROTECT,
                                verbose_name="Programa educativo",
                                blank=True,
                                null=True)
    academy = models.ForeignKey(Academy,
                                on_delete=models.PROTECT,
                                verbose_name="Cuerpo académico",
                                blank=True,
                                null=True)
    numEmp = models.CharField(max_length=20,
                              verbose_name="Numero de empleado",
                              blank=True,)
    firstName = models.CharField(max_length=50,
                                 verbose_name="Nombre(s)",
                                 blank=True)
    lastNameA = models.CharField(max_length=50,
                                 verbose_name="Apellido Paterno",
                                 blank=True)
    lastNameB = models.CharField(max_length=50,
                                 verbose_name="Apellido Materno",
                                 blank=True)
    author_info = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name=
        "Define esta cuenta con un registro en la tabla de autores",
        null=True)
    timeStamp = models.DateTimeField(auto_now_add=True,
                                     verbose_name="Time Stamp")

    def __str__(self):
        return f'{self.firstName} {self.lastNameA} {self.lastNameB}'

    def get_absolute_url(self):
        return reverse("userSap:account-detail", kwargs={"id": self.id})

    class Meta:
        verbose_name = 'Cuenta'


class UserSap(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100,
                              verbose_name="Correo UABC",
                              unique=True)
    account = models.OneToOneField(Account,
                                   on_delete=models.CASCADE,
                                   verbose_name="Informacion personal",
                                   blank=True,
                                   null=True)
    statuSelect = (
        (None, 'Selecciona estado'),
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )
    status = models.CharField(max_length=25,
                              choices=statuSelect,
                              verbose_name="Estado",
                              blank=True)
    rolSelect = (
        (None, 'Seleccionar rol'),
        ('Profesor/Investigador', 'Profesor/Investigador'),
        ('Tecnico academico', 'Tecnico academico'),
        ('Estudiante licenciatura', 'Estudiante licenciatura'),
        ('Estudiante postgrado', 'Estudiante postgrado'),
    )
    rol = models.CharField(max_length=25,
                           choices=rolSelect,
                           verbose_name="Rol en UABC")

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=
        _('IMPORTANTE. Marcar esta casilla le da al usuario acceso completo a  este sitio de administracion.'
          ),
    )

    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'),
    )

    timeStamp = models.DateTimeField(auto_now_add=True,
                                     verbose_name="Time Stamp")
    image = models.ImageField(blank=True,
                              default='default_profile.jpg',
                              upload_to='profile_images',
                              verbose_name="Imagen del perfil")

    objects = UserSapManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rol']

    def __str__(self):
        return f'{self.account.firstName} {self.account.lastNameA} {self.account.lastNameB}'

    def get_full_name(self):
        return self.account

    def get_short_name(self):
        return self.account.firstName
        #return "just a blank name pls"

    def get_absolute_url(self):
        return reverse("userSap:user-index")

    class Meta:
        verbose_name = 'Usuario'
