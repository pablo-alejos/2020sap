from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse, reverse_lazy

from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import UserSap
from .models import Account, Academy, Program


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Correo'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class UserSapModelForm(forms.ModelForm):
    class Meta:
        model = UserSap
        fields = ['account',
                  'status',
                  'email',
                  'rol',
                  ]


class UserSapCreationForm(UserCreationForm):
    """A form for creating new users. Includes all the required
     fields, plus a repeated password."""
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmar contraseña', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserSapCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['rol'].widget.attrs['class'] = 'custom-select custom-select-sm'
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-sm'

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email in UserSap.objects.values_list('email', flat=True):
            raise forms.ValidationError(
                "Este correo electronico ya esta en uso. Eliga uno distinto.")
        return email

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserSapCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class Meta:
        model = UserSap
        fields = [
            # 'account',
            'email',
            'rol',
        ]


class UserSapChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kwargs):
        super(UserSapChangeForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['rol'].widget.attrs['class'] = 'custom-select custom-select-sm'

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

    class Meta:
        model = UserSap
        fields = ('account',
                  'email',
                  'rol',
                  'password'
                  )

class AccountModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AccountModelForm, self).__init__(*args, **kwargs)
        self.fields['program'].widget.attrs['class'] = 'custom-select custom-select-sm'
        self.fields['academy'].widget.attrs['class'] = 'custom-select custom-select-sm'
        self.fields['numEmp'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['firstName'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['lastNameA'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['lastNameB'].widget.attrs['class'] = 'form-control form-control-sm'

    class Meta:
        model = Account
        fields = ['program',
                  'academy',
                  'numEmp',
                  'firstName',
                  'lastNameA',
                  'lastNameB']

class AcademyModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AcademyModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control form-control-sm'

    class Meta:
        model = Academy
        fields = ['name']

class ProgramModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProgramModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['key'].widget.attrs['class'] = 'form-control form-control-sm'

    class Meta:
        model = Program
        fields = ['name',
                  'key']
