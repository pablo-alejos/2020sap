from django import forms
from django.forms import ModelForm

from .models import BookChapter
from project.models import Project
from userSap.models import UserSap
from account.models import Account, Program, Academy
from author.models import Author
from event.models import Event
from tag.models import Tag


class BookChapterModelForm(forms.ModelForm):

    project = forms.ModelChoiceField(
        queryset=Project.objects.order_by('title'),
        required=False,
        label="Proyecto",
        empty_label="Seleccionar proyecto",
        widget=forms.Select(
            attrs={
                "class": "basic-single form-control w-100",
                "id": "id-select-project-bookchapter"
            }))
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.order_by('firstName'),
        label="Autores",
        widget=forms.SelectMultiple(
            attrs={
                "class": "basic-multiple form-control w-100",
                "multiple ": "multiple ",
                "id": "id-select-bookChapter-authors"
            }))
    title = forms.CharField(label="Titulo",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Inserte su titulo aqui",
                                    "class": "form-control form-control-sm",
                                    "id": "my-id-title-bookChapter"
                                }))
    bookTitle = forms.CharField(
        label="Titulo del libro",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Inserte su titulo aqui",
                "class": "form-control form-control-sm",
                "id": "my-id-bookTitle-bookChapter"
            }))
    bookEditorial = forms.CharField(
        label="Editorial del libro",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Inserte la editorial aqui",
                "class": "form-control form-control-sm",
                "id": "my-id-bookeditorial"
            }))
    bookIsbn = forms.CharField(label="ISBN del libro",
                               required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "Inserte el ISBN aqui",
                                       "class": "form-control form-control-sm",
                                       "id": "my-id-bookisbn"
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
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.filter(tag="lgac"),
        required=False,
        label="Etiquetas",
        widget=forms.SelectMultiple(
            attrs={
                "class": "basic-multiple form-control w-100",
                "multiple ": "multiple ",
                "id": "id-select-book-tags"
            }))
    programTribute = forms.ModelChoiceField(
        queryset=Program.objects.order_by('name'),
        label="Programa educativo al que tributa",
        empty_label="Ninguno",
        widget=forms.Select(
            attrs={
                "class": "basic-single form-control w-100",
                "id": "id-select-programTribute-book"
            }))
    academyTribute = forms.ModelChoiceField(
        queryset=Academy.objects.order_by('name'),
        required=False,
        label="Cuerpo academico al que tributa",
        empty_label="Ninguno",
        widget=forms.Select(
            attrs={
                "class": "basic-single form-control w-100",
                "id": "id-select-academyTribute-book"
            }))
    eventPublication = forms.ModelChoiceField(
        queryset=Event.objects.order_by('name'),
        required=False,
        label="Evento en el que fue publicado",
        empty_label="Ninguno",
        widget=forms.Select(
            attrs={
                "class": "basic-single form-control w-100",
                "id": "id-select-eventPublication-book"
            }))

    class Meta:
        model = BookChapter
        fields = [
            'user','project', 'authors', 'title', 'bookTitle', 'bookEditorial',
            'bookIsbn', 'publicationYear', 'tags', 'programTribute',
            'academyTribute', 'eventPublication', 'image', 'file'
        ]

    def __init__(self, *args, **kwargs):
        super(BookChapterModelForm, self).__init__(*args, **kwargs)
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

    def clean_title(self):
        title = self.cleaned_data.get("title")
        return title

    def clean_isbn(self):
        isbn = self.cleaned_data.get("isbn")
        if len(isbn) > 17 or len(isbn) < 13:
            raise forms.ValidationError(
                "El ISBN debe seguir las reglas de numeracion internacional.")
        return isbn

    def clean_project(self):
        project = self.cleaned_data.get("project")
        user = self.cleaned_data.get("user")
        if project:
            projectObj = Project.objects.get(id=project.id)
            if not user in projectObj.participants.all():
                raise forms.ValidationError(
                    "Usted no es participante en este proyecto.")
        return project

    def clean(self):
        cleaned_data = super().clean()
        editorial = cleaned_data.get("editorial")
        event = cleaned_data.get("event")

        if editorial and event:
            msg = "Solo puede tener una fuente la publicación de este producto."
            self.add_error('editorial', msg)
            self.add_error('event', msg)

