from django import forms
from django.forms import ModelForm

from .models import Event

class EventModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EventModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['eventCreated'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['eventFinish'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['topic'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['headquarters'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['address'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['event'].widget.attrs['class'] = 'custom-select custom-select-sm'
       
    class Meta:
        model = Event
        fields = ['name',
                  'eventCreated',
                  'eventFinish',
                  'topic',
                  'headquarters',
                  'address',
                  'event']

