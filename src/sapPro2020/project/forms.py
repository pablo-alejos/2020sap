from django import forms
from django.forms import ModelForm

from .models import Project
from account.models import Account
from userSap.models import UserSap


class ProjectModelForm(forms.ModelForm):
    title = forms.CharField(label="Nombre del proyecto",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Inserte el nombre aqui",
                                    "class": "form-control form-control-sm",
                                    "id": "id-name-proyect"
                                }))
    announcement = forms.CharField(
        required=False,
        label="Convocatoria",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Inserte la convocatoria",
                "class": "form-control form-control-sm ",
                "id": "id-announcement-project"
            }))
    amount = forms.IntegerField(
        required=False,
        label="Presupuesto",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Ingrese el presupuesto aqui",
                "class": "form-control form-control-sm",
                "id": "id-amount-project"
            }))
    participants = forms.ModelMultipleChoiceField(
        queryset=UserSap.objects.all(),
        label="Participantes",
        widget=forms.SelectMultiple(
            attrs={
                "class": "basic-multiple form-control w-100",
                "multiple ": "multiple ",
                "id": "id-participans-project"
            }))
    code = forms.IntegerField(label="Clave",
                              widget=forms.NumberInput(
                                  attrs={
                                      "placeholder": "Ingrese la clave aqui",
                                      "class": "form-control form-control-sm"
                                  }))
    vigent = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
        attrs={"class": "custom-select custom-select-sm"}))

    def __init__(self, *args, **kwargs):
        super(ProjectModelForm, self).__init__(*args, **kwargs)
        self.fields['typeP'].widget.attrs[
            'class'] = 'custom-select custom-select-sm'
        self.fields['status'].widget.attrs[
            'class'] = 'custom-select custom-select-sm'
        for field in self.fields.values():
            field.error_messages = {
                'required':
                'El campo {fieldname} es requerido'.format(
                    fieldname=field.label)
            }

    class Meta:
        model = Project
        fields = [
            'userResponsable', 'typeP', 'title', 'announcement', 'amount',
            'participants', 'code', 'vigent', 'status'
        ]
