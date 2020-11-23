from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserSapCreationForm, UserSapChangeForm

from .models import UserSap


class UserSapAdmin(UserAdmin):
    add_form = UserSapCreationForm
    form = UserSapChangeForm
    model = UserSap
    list_display = ('email', 'account', 'rol', 'is_staff', 'is_active',)
    list_filter = ('email', 'account', 'rol', 'is_staff', 'is_active',)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'rol',)}),
        ('Personal info', {'fields': ('account',)}),
        ('Gruops', {'fields': ('groups',)}),
        ('User permissions', {'fields': ('user_permissions',)}),
        ('Login', {'fields': ('is_active',)}),
        ('Staff', {'fields': ('is_staff',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'account', 'rol', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )

    ordering = ('email',)

    search_fields = ('email',)

    filter_horizontal = ()


admin.site.register(UserSap, UserSapAdmin)