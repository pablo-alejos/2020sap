from django import forms
from django.forms import ModelForm

from .models import Book
from project.models import Project
from userSap.models import UserSap
from account.models import Account, Program, Academy
from event.models import Event
from tag.models import Tag


class BookModelForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.order_by('title'),
                                     label="Proyecto",
                                     empty_label="Seleccionar proyecto",
                                     widget=forms.Select(
                                         attrs={
                                             "class": "basic-single form-control w-100",
                                             "id": "id-select-project-book"}))
    authors = forms.ModelMultipleChoiceField(queryset=Account.objects.order_by('firstName'),
                                             label="Autores",
                                             widget=forms.SelectMultiple(
                                                 attrs={
                                                     "class": "basic-multiple form-control w-100",
                                                     "multiple ": "multiple ",
                                                     "id": "id-select-book-authors"}))
    title = forms.CharField(label="Titulo",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Inserte su titulo aqui",
                                    "class": "form-control form-control-sm",
                                    "id": "my-id-title"}))
    editorial = forms.CharField(label="Editorial",
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "Inserte la editorial aqui",
                                        "class": "form-control form-control-sm",
                                        "id": "my-id-editorial"}))
    isbn = forms.CharField(label="ISBN",
                           widget=forms.TextInput(
                               attrs={
                                   "placeholder": "Inserte el ISBN aqui",
                                   "class": "form-control form-control-sm",
                                   "id": "my-id-isbn"}))

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
    publicationYear = forms.CharField(label="Año de publicacion",
                                      widget=forms.Select(
                                          choices=YEARS,
                                          attrs={
                                              "placeholder": "Inserte el año de publicacion aqui",
                                              "class": "basic-single form-control form-control-sm w-100",
                                              "id": "my-id-pubyear"}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag="lgac"),
                                          label="Etiquetas",
                                          widget=forms.SelectMultiple(
                                              attrs={
                                                "class": "basic-multiple form-control w-100",
                                                "multiple ": "multiple ",
                                                "id": "id-select-book-tags"}))
    programTribute = forms.ModelChoiceField(queryset=Program.objects.order_by('name'),
                                            label="Programa educativo al que tributa",
                                            empty_label="Ninguno",
                                            widget=forms.Select(
                                                        attrs={
                                                            "class": "basic-single form-control w-100",
                                                            "id": "id-select-programTribute-book"}))
    academyTribute = forms.ModelChoiceField(queryset=Academy.objects.order_by('name'),
                                            label="Cuerpo academico al que tributa",
                                            empty_label="Ninguno",
                                            widget=forms.Select(
                                                        attrs={
                                                            "class": "basic-single form-control w-100",
                                                            "id": "id-select-academyTribute-book"}))
    eventPublication = forms.ModelChoiceField(queryset=Event.objects.order_by('name'),
                                            label="Evento en el que fue publicado",
                                            empty_label="Ninguno",
                                            widget=forms.Select(
                                                        attrs={
                                                            "class": "basic-single form-control w-100",
                                                            "id": "id-select-eventPublication-book"}))
    
    class Meta:
        model = Book
        fields = ['project',
                  'authors',
                  'title',
                  'editorial',
                  'isbn',
                  'publicationYear',
                  'tags',
                  'programTribute',
                  'academyTribute',
                  'eventPublication',
                  'file']

    def __init__(self, *args, **kwargs):
        super(BookModelForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs['class'] = 'form-control-file'

    def clean(self):
        super(BookModelForm, self).clean()
        project = self.cleaned_data.get("project")
        authors = self.cleaned_data.get("authors")
        title = self.cleaned_data.get("title")
        editorial = self.cleaned_data.get("editorial")
        isbn = self.cleaned_data.get("isbn")
        publicationYear = self.cleaned_data.get("publicationYear")
        tags = self.cleaned_data.get("tags")
        file = self.cleaned_data.get("file")