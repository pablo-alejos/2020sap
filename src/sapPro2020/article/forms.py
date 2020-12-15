from django import forms
from django.forms import ModelForm

from .models import Article, Journal
from project.models import Project
from userSap.models import UserSap
from account.models import Account, Program, Academy
from author.models import Author
from tag.models import Tag
from event.models import Event


class ArticleModelForm(forms.ModelForm):
    project = forms.ModelChoiceField(
        queryset=Project.objects.order_by('title'),
        required=False,
        label="Proyecto",
        empty_label="Seleccionar proyecto",
        widget=forms.Select(
            attrs={
                "class": "basic-single form-control w-100",
                "id": "id-select-project-article"
            }))
    journal = forms.ModelChoiceField(
        queryset=Journal.objects.all(),
        label="Revista",
        empty_label="Seleccionar revista",
        widget=forms.Select(
            attrs={
                "class": "basic-single form-control w-100",
                "id": "id-select-journal-article"
            }))
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.order_by('firstName'),
        label="Autores",
        widget=forms.SelectMultiple(
            attrs={
                "class": "basic-multiple form-control w-100",
                "multiple ": "multiple ",
                "id": "id-select-article-authors"
            }))
    title = forms.CharField(label="Título",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Inserte su título aqui",
                                    "class": "form-control form-control-sm",
                                    "id": "id-title-article"
                                }))
    indexed = forms.BooleanField(
        required=False,
        label="Indizado",
        widget=forms.CheckboxInput(attrs={
            "class": "",
            "id": "my-id-indexed-article"
        }))
    indexInfo = forms.CharField(
        required=False,
        label="Donde",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Inserte donde esta indizado aqui",
                "class": "form-control form-control-sm",
                "id": "my-id-indexinfo-article"
            }))
    arbitration = forms.BooleanField(
        required=False,
        label="Arbitration",
        widget=forms.CheckboxInput(attrs={
            "class": "",
            "id": "my-id-arbitration-article"
        }))
    YEARS = (
        ('1990', '1990'),
        ('1991', '1991'),
        ('1992', '1992'),
        ('1993', '1993'),
        ('1993', '1993'),
        ('1995', '1995'),
        ('1995', '1995'),
        ('1997', '1997'),
        ('1998', '1998'),
        ('1999', '1999'),
        ('2000', '2000'),
        ('2001', '2001'),
        ('2002', '2002'),
        ('2003', '2003'),
        ('2004', '2004'),
        ('2005', '2005'),
        ('2006', '2006'),
        ('2007', '2007'),
        ('2008', '2008'),
        ('2009', '2009'),
        ('2010', '2010'),
        ('2011', '2011'),
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
    )
    publicationYear = forms.CharField(
        label="Año de publicacion",
        widget=forms.Select(
            choices=YEARS,
            attrs={
                "placeholder": "Inserte el año de publicacion aqui",
                "class": "basic-single form-control form-control-sm w-100",
                "id": "my-id-pubyear"
            }))
    pages = forms.CharField(
        label="Paginas",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Inserte el numero de paginas aqui",
                "class": "form-control form-control-sm",
                "id": "my-id-pages-article"
            }))
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.filter(tag="lgac"),
        required=False,
        label="Etiquetas",
        widget=forms.SelectMultiple(
            attrs={
                "class": "basic-multiple form-control w-100",
                "multiple ": "multiple ",
                "id": "id-select-article-tags"
            }))
    programTribute = forms.ModelChoiceField(
        queryset=Program.objects.order_by('name'),
        label="Programa educativo al que tributa",
        empty_label="Ninguno",
        widget=forms.Select(
            attrs={
                "class": "basic-single form-control w-100",
                "id": "id-select-programTribute-article"
            }))
    academyTribute = forms.ModelChoiceField(
        queryset=Academy.objects.order_by('name'),
        required=False,
        label="Cuerpo academico al que tributa",
        empty_label="Ninguno",
        widget=forms.Select(
            attrs={
                "class": "basic-single form-control w-100",
                "id": "id-select-academyTribute-article"
            }))
    eventPublication = forms.ModelChoiceField(
        queryset=Event.objects.order_by('name'),
        required=False,
        label="Evento en el que fue publicado",
        empty_label="Ninguno",
        widget=forms.Select(
            attrs={
                "class": "basic-single form-control w-100",
                "id": "id-select-eventPublication-article"
            }))

    def __init__(self, *args, **kwargs):
        super(ArticleModelForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'form-control-file'
        self.fields['image'].widget.attrs['accept'] = 'image/*'
        self.fields['file'].widget.attrs['class'] = 'form-control-file'
        self.fields['file'].widget.attrs['accept'] = 'application/pdf'
        for field in self.fields.values():
            field.error_messages = {
                'required':
                'El campo {fieldname} es requerido'.format(
                    fieldname=field.label)
            }

    def clean_project(self):
        project = self.cleaned_data.get("project")
        user = self.cleaned_data.get("user")
        if project:
            projectObj = Project.objects.get(id=project.id)
            if not user in projectObj.participants.all():
                raise forms.ValidationError(
                    "Usted no es participante en este proyecto.")
        return project

    class Meta:
        model = Article
        fields = [
            'user', 'project', 'journal', 'authors', 'title', 'indexed',
            'indexInfo', 'arbitration', 'publicationYear', 'pages', 'file', 'image',
            'programTribute', 'academyTribute', 'eventPublication', 'tags'
        ]


class JournalModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JournalModelForm, self).__init__(*args, **kwargs)
        self.fields['quartMagazine'].widget.attrs[
            'class'] = 'custom-select custom-select-sm'
        for field in self.fields.values():
            field.error_messages = {
                'required':
                'El campo {fieldname} es requerido'.format(
                    fieldname=field.label)
            }

    name = forms.CharField(label="Título",
                           widget=forms.TextInput(
                               attrs={
                                   "placeholder": "Inserte su nombre aqui",
                                   "class": "form-control form-control-sm",
                                   "id": "id-name-journal"
                               }))
    editorial = forms.CharField(
        label="Editorial",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Inserte la editorial aqui",
                "class": "form-control form-control-sm",
                "id": "id-editorial-journal"
            }))
    country = forms.CharField(label="País",
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "Inserte su título aquí",
                                      "class": "form-control form-control-sm",
                                      "id": "id-country-journal"
                                  }))
    issn = forms.CharField(label="ISSN",
                           widget=forms.TextInput(
                               attrs={
                                   "placeholder": "Inserte el ISSN aqui",
                                   "class": "form-control form-control-sm",
                                   "id": "id-issn-journal"
                               }))
    referenceMagazine = forms.CharField(
        label="Referencia (enlace) a la revista",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Inserte referencia (enlace) aqui",
                "class": "form-control form-control-sm",
                "id": "id-referenceMagazine-journal"
            }))

    class Meta:
        model = Journal
        fields = [
            'name', 'editorial', 'country', 'quartMagazine',
            'referenceMagazine', 'issn'
        ]
