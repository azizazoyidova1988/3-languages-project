from django import forms
from .models import *


class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact()
        fields = '__all__'
