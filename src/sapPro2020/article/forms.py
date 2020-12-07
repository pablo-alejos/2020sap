from django import forms
from django.forms import ModelForm

from .models import Article, Journal
from project.models import Project
from userSap.models import UserSap
from account.models import Account


class ArticleModelForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(),
                                     label="Proyecto",
                                     empty_label="Seleccionar Proyecto",
                                     widget=forms.Select(
                                         attrs={"class": "selectpicker form-control",
                                                "data-style": "btn-outline",
                                                "multiple data-live-search": "true",
                                                "data-max-options": "1",
                                                "data-size": "5",
                                                "data-live-search-normalize": "true",
                                                "id": "id-select-project-article"}))
    journal = forms.ModelChoiceField(queryset=Journal.objects.all(),
                                     label="Revista",
                                     empty_label="Seleccionar Revista",
                                     widget=forms.Select(
                                         attrs={"class": "selectpicker form-control",
                                                "multiple data-live-search": "true",
                                                "data-style": "btn-outline",
                                                "data-size": "5",
                                                "data-live-search-normalize": "true",
                                                "data-max-options": "1",
                                                "data-none-selected-text": "Nada seleccionado",
                                                "id": "id-select-journal-article"}))
    
    authors = forms.ModelMultipleChoiceField(queryset=Account.objects.all(),
                                             label="Autores",
                                             widget=forms.SelectMultiple(
                                                 attrs={
                                                     "class": "selectpicker form-control",
                                                     "multiple data-live-search": "true",
                                                     "data-style": "btn-outline",
                                                     "data-size": "5",
                                                     "data-live-search-normalize": "true",
                                                     "data-selected-text-format": "count > 2",
                                                     "data-none-selected-text": "Nada seleccionado",
                                                     "id": "id-select-book-authors"}))
    title = forms.CharField(label="Título",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder":"Inserte su título aqui",
                                    "class":"form-control",
                                    "id":"my-id-title-article"
                                }))
    indexed = forms.BooleanField(label="Indizado",
                            widget=forms.CheckboxInput(
                                attrs={
                                    "class":"form-control",
                                    "id":"my-id-indexed-article"
                                }))
    indexInfo = forms.CharField(label="Donde",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder":"Inserte donde esta indizado aqui",
                                    "class":"form-control",
                                    "id":"my-id-indexinfo-article"
                                }))
    arbitration = forms.BooleanField(label="Arbitration",
                            widget=forms.CheckboxInput(
                                attrs={
                                    "class":"form-control",
                                    "id":"my-id-arbitration-article"
                                }))
    month = forms.CharField(label="Mes",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder":"Inserte el mes de publicacion aqui",
                                    "class":"form-control",
                                    "id":"my-id-month-article"
                                }))
    year = forms.CharField(label="Año de publicacion",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder":"Inserte el año de publicacion aqui",
                                    "class":"form-control",
                                    "id":"my-id-pubyear-article"
                                }))
   
    pages = forms.CharField(label="Paginas",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder":"Inserte el numero de paginas aqui",
                                    "class":"form-control",
                                    "id":"my-id-pages-article"
                                }))
    
    def __init__(self, *args, **kwargs):
        super(ArticleModelForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs['class'] = 'form-control-file'
    

    class Meta:
        model = Article
        fields = ['project',
                  'journal',
                  'authors',
                  'title',
                  'indexed',
                  'indexInfo',
                  'arbitration',
                  'month',
                  'year',
                  'pages',
                  'file']


class JournalModelForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['name',
                  'editorial',
                  'country',
                  'issn']
