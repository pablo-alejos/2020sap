from django import forms
from django.forms import ModelForm

from .models import Forum,Symposium,Congress

class ForumModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ForumModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['eventCreated'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['topic'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['headquarters'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['address'].widget.attrs['class'] = 'form-control form-control-sm'
       

    class Meta:
        model = Forum
        fields = ['name',
                  'eventCreated',
                  'topic',
                  'headquarters',
                  'address']


class SymposiumModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SymposiumModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['eventCreated'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['topic'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['headquarters'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['address'].widget.attrs['class'] = 'form-control form-control-sm'
    class Meta:
        model = Symposium
        fields = ['name',
                  'eventCreated',
                  'topic',
                  'headquarters',
                  'address']

class CongressModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CongressModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['eventCreated'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['topic'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['headquarters'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['address'].widget.attrs['class'] = 'form-control form-control-sm'

    class Meta:
        model = Congress
        fields = ['name',
                  'eventCreated',
                  'topic',
                  'headquarters',
                  'address']