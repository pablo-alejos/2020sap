from django import forms
from django.forms import ModelForm

from .models import Account, Academy, Program


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