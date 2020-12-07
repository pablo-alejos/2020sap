from django import forms
from django.forms import ModelForm

from .models import Project
from account.models import Account


class ProjectModelForm(forms.ModelForm):
    userResponsable = forms.ModelChoiceField(queryset=Account.objects.all(),
                                             label="Responsable Tecnico",
                                             empty_label="Seleccione Responsable",
                                             widget=forms.Select(
                                                 attrs={
                                                     "class": "basic-single form-control w-100",
                                                     "id": "id-responsable"
                                                 }))
    title = forms.CharField(label="Nombre del proyecto",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Inserte el nombre aqui",
                                    "class": "form-control form-control-sm",
                                    "id": "id-name-proyect"
                                }))
    announcement = forms.CharField(label="Convocatoria",
                                   widget=forms.TextInput(
                                       attrs={
                                           "placeholder": "Inserte la convocatoria",
                                           "class": "form-control form-control-sm",
                                           "id": "id-announcement-project"
                                       }))
    amount = forms.IntegerField(label="Presupuesto",
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "Ingrese el presupuesto aqui",
                                        "class": "form-control form-control-sm",
                                        "id": "id-amount-project"
                                    }))
    participants = forms.ModelMultipleChoiceField(queryset=Account.objects.order_by('firstName'),
                                                  label="Participantes",
                                                  widget=forms.SelectMultiple(
                                                      attrs={
                                                          "class": "basic-multiple form-control w-100",
                                                          "multiple ": "multiple ",
                                                          "id": "id-participans-project"}))
    code = forms.IntegerField(label="Codigó",
                              widget=forms.NumberInput(
                                  attrs={
                                      "placeholder": "Ingrese el codigo aqui",
                                      "class": "form-control form-control-sm"
                                  }))

    def clean(self):
        super(ProjectModelForm, self).clean()
        userResponsable = self.cleaned_data.get("userResponsable")
        typeP = self.cleaned_data.get("typeP")
        title = self.cleaned_data.get("title")
        announcement = self.cleaned_data.get("announcement")
        amount = self.cleaned_data.get("amount")
        participants = self.cleaned_data.get("participants")
        code = self.cleaned_data.get("code")
        vigent = self.cleaned_data.get("vigent")
        status = self.cleaned_data.get("status")

    class Meta:
        model = Project
        fields = ['userResponsable',
                  'typeP',
                  'title',
                  'announcement',
                  'amount',
                  'participants',
                  'code',
                  'vigent',
                  'status']
