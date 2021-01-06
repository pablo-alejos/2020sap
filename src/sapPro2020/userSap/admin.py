from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserSapCreationForm, UserSapChangeForm

from .models import UserSap

from .models import Account
from .models import Academy
from .models import Program


class UserSapAdmin(UserAdmin):
    add_form = UserSapCreationForm
    form = UserSapChangeForm
    model = UserSap
    verbose_name = 'Usuario Sap'
    list_display = (
        'email',
        'account',
        'rol',
        'is_staff',
        'is_active',
    )
    list_filter = (
        'rol',
        'is_staff',
        'is_active',
    )

    fieldsets = (
        ('Usuario Sap', {
            'fields': (
                'email',
                'password',
                'rol',
            )
        }),
        ('Informacion personal', {
            'fields': ('account', )
        }),
        ('Grupos', {
            'classes': ('wide', ),
            'fields': ('groups', )
        }),
        ('Permisos', {
            'classes': ('wide', ),
            'fields': ('user_permissions', )
        }),
        ('Login', {
            'fields': ('is_active', )
        }),
        ('Staff', {
            'fields': ('is_staff', )
        }),
    )
    """
    add_fieldsets = (
        ('add', {
            'classes': ('wide',),
            'fields': ('email', 'account', 'rol', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
"""
    ordering = ('email', )

    search_fields = ('email', )

    filter_horizontal = ()


admin.site.register(UserSap, UserSapAdmin)

admin.site.register(Account)
admin.site.register(Academy)
admin.site.register(Program)