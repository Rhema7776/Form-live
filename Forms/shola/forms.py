from django import forms
from django.forms import ModelForm
from .models import User

# Create a user form
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('First_name', 'Last_name', 'des', 'phone')
        #To remove the labels
        labels =  {
            'First_name': '',
            'Last_name': '',
            'des': '',
            'phone': '',
        }

        widgets = {
            'First_name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'First name'}),
            'Last_name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'last name'}),
            'des': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Describe yourself'}),
            'phone': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Phone number'}),
        }