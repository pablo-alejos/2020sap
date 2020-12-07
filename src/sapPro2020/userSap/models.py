from django.db import models
from django.urls import reverse, reverse_lazy

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import Account

from .managers import UserSapManager


class UserSap(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, verbose_name="Correo UABC", unique=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, verbose_name="Informacion personal", blank=True, null=True)
    statuSelect = (
        (None, 'Selecciona estado'),
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )
    status = models.CharField(max_length=25, choices=statuSelect, verbose_name="Estado", blank=True)
    rolSelect = (
        (None, 'Seleccionar rol'),
        ('Profesor/Investigador', 'Profesor/Investigador'),
        ('Tecnico academico', 'Tecnico academico'),
        ('Estudiante licenciatura', 'Estudiante licenciatura'),
        ('Estudiante postgrado', 'Estudiante postgrado'),
    )
    rol = models.CharField(max_length=25, choices=rolSelect, verbose_name="Rol en UABC")

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('IMPORTANTE. Marcar esta casilla le da al usuario acceso completo a  este sitio de administracion.'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    timeStamp = models.DateTimeField(auto_now_add=True, verbose_name="Time Stamp")
    image = models.ImageField(blank=True,default='default_profile.jpg', upload_to='profile_images',verbose_name="Imagen del perfil")

    objects = UserSapManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rol']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.account

    def get_short_name(self):
        return self.account.firstName
        #return "just a blank name pls"

    def get_absolute_url(self):
        return reverse("userSap:user-index")
    
    class Meta:
        verbose_name = 'Usuario'