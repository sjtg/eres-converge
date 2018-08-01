from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



Portal = [
    ('student', 'Students'),
    ('reviewer', 'Reviewer'),
]

class SignUpForm(UserCreationForm):
    FirstName = forms.CharField(max_length=30, required=False, help_text='First name')
    LastName = forms.CharField(max_length=30, required=False, help_text='Last name')
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    telephone = forms.CharField(max_length=30, required=False, help_text='Telephone')
    portals = forms.CharField(label='Select which occupation', widget=forms.Select(choices=Portal))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','telephone','portals', 'password1', 'password2', )



# class SignUpForm(UserCreationForm):
# 	email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
#
# 	class Meta:
# 		model = User
# 		fields = ('username', 'email', 'password1', 'password2')
