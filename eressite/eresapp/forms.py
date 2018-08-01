from django.core.files import File
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'blog_images')

class DocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ('title','reference','description', 'docs')

class ReviewerForm(forms.ModelForm):
    class Meta:
        model = Reviewer
        fields = ('title','reference','comments', 'docs')


class FeesForm(forms.ModelForm):
    class Meta:
        model = Fees
        fields = ('title', 'name', 'prices' )
