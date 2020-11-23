from django import forms
from django.forms import ModelForm

from .models import Tag


class TagModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TagModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control form-control-sm'

    class Meta:
        model = Tag
        fields = ['name',
                  'tag']