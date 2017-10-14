from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.models import User

from .models import Post

from .models import Photo

Portal = [
    ('student', 'Students'),
    ('reviewer', 'Reviewer'),
]

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='First name')
    last_name = forms.CharField(max_length=30, required=False, help_text='Last name')
    email = forms.EmailField(max_length=254, help_text='Required')
    telephone = forms.CharField(max_length=30, required=False, help_text='Telephone')
    portals = forms.CharField(label='Select which occupation', widget=forms.Select(choices=Portal))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','telephone','portals', 'password1', 'password2', )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file', )
