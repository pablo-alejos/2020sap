from django import forms
from django.forms import ModelForm

from .models import BookChapter
from project.models import Project
from userSap.models import UserSap
from account.models import Account


class BookChapterModelForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(),
                                     label="Proyecto",
                                     empty_label="Seleccionar proyecto",
                                     widget=forms.Select(
                                         attrs={
                                             "class": "selectpicker form-control",
                                             "data-style": "btn-outline",
                                             "multiple data-live-search": "true",
                                             "data-max-options": "1",
                                             "data-size": "5",
                                             "data-live-search-normalize": "true",
                                             "id": "id-select-project-book"}))
    authors = forms.ModelMultipleChoiceField(queryset=Account.objects.all(),
                                             label="Autores",
                                             widget=forms.SelectMultiple(
                                                 attrs={
                                                     "class": "my-selectpicker form-control",
                                                     "multiple data-live-search": "true",
                                                     "data-style": "btn-outline",
                                                     "data-size": "5",
                                                     "data-live-search-normalize": "true",
                                                     "data-selected-text-format": "count > 2",
                                                     "data-none-selected-text": "Nada seleccionado",
                                                     "id": "id-select-book-authors"}))
    """user = forms.ModelChoiceField(queryset=UserSap.objects.all(),
                                  label="Autor",
                                  empty_label="Seleccionar autor principal",
                                  widget=forms.Select(
                                      attrs={
                                          "class": "my-selectpicker form-control",
                                          "data-style": "btn-outline",
                                          "multiple data-live-search": "true",
                                          "data-max-options": "1",
                                          "data-size": "5",
                                          "data-live-search-normalize": "true",
                                          "id": "id-select-book-user"}))"""
    title = forms.CharField(label="Titulo",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Inserte su titulo aqui",
                                    "class": "form-control",
                                    "id": "my-id-title"}))
    bookTitle = forms.CharField(label="Titulo del libro",
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "Inserte el titulo del libro aqui",
                                        "class": "form-control",
                                        "id": "my-id-bookTitle"}))
    bookEditorial = forms.CharField(label="Editorial del libro",
                                    widget=forms.TextInput(
                                        attrs={
                                            "placeholder": "Inserte la editorial del libro aqui",
                                            "class": "form-control",
                                            "id": "my-id-isbn"}))

    bookIsbn = forms.CharField(label="ISBN del libro",
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "Inserte el ISBN del libro aqui",
                                       "class": "form-control",
                                       "id": "my-id-pubyear"}))

    def __init__(self, *args, **kwargs):
        super(BookChapterModelForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs['class'] = 'form-control-file'

    class Meta:
        model = BookChapter
        fields = ['project',
                  # 'user',
                  'authors',
                  'title',
                  'bookTitle',
                  'bookEditorial',
                  'bookIsbn',
                  'file']