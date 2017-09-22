# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate

from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect, HttpResponse

from django.utils import timezone
from .models import Post

from .forms import PostForm

from django.http import JsonResponse
from django.views import View

from .forms import PhotoForm
from .models import Photo


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form  = UserCreationForm(request.POST)
	if form.is_valid():
 	    form.save()
	    username = form.cleaned_data.get('username')
	    raw_passwprd = form.cleaned_data.get('password')
	    user = authenticate(username=username, password=raw_password)
	    login(request, user)
	    return redirect('home')
	else:
	    form = UserCreationForm()

	return render(request, 'site/signup.html', {'form':form})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'site/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'site/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'site/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(request.POST, instance=post)
    return render(request, 'site/post_edit.html', {'form': form})


class UploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'site/index.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse({'message': 'Success'})
