from django import forms
from django.forms import ModelForm
from .models import Author

class AuthorModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AuthorModelForm, self).__init__(*args, **kwargs)
        self.fields['firstName'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['lastNameA'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['lastNameB'].widget.attrs['class'] = 'form-control form-control-sm'

    class Meta:
        model = Author
        fields = ['firstName',
                  'lastNameA',
                  'lastNameB']