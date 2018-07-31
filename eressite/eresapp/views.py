# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required

from .forms import SignUpForm

from django.contrib.auth.models import User

# from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import get_object_or_404 , render, redirect

from django.utils import timezone
from .models import Post

from .forms import PostForm

from django.http import JsonResponse
from django.views import View



from .forms import DocumentForm
from .models import Document


# Create your views here.

def home(request):
	return render(request, 'site/index.html', {})

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		# profile = Profile.objects.get(user = request.user)
		if form.is_valid():
		  form.save()
		  username = form.cleaned_data.get('username')
	          raw_password = form.cleaned_data.get('password1')
		  user = authenticate(username=username, password=raw_password)
		  login(request, user)
		  return redirect('dashboard')
	else:
	    form = SignUpForm()
	return render(request, 'site/signup.html', {'form':form})




@login_required(login_url='login')
def dashboard(request):
	document_list = Document.objects.all()
        return render(request, 'site/dashboard.html', {'documents': document_list})
	#return render(request, 'site/dashboard.html')
@login_required(login_url='login')
def dashboard_reviewer(request):
	document_list = Document.objects.all()
        return render(request, 'site/reviewer.html', {'documents': document_list})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'site/board.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'site/post_detail.html', {'post': post})

@login_required(login_url='login')
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(request.POST)
    return render(request, 'site/post_edit.html', {'form': form})


@login_required(login_url='login')
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
        form = PostForm(instance=post)
    return render(request, 'site/post_edit.html', {'form': form})


def about(request):
	return render(request, 'site/aboutus.html', {})

def fees(request):
	return render(request, 'site/fees.html', {})

class UploadView(View):
    	def get(self, request):
	        document_list = Document.objects.all()
	        return render(self.request, 'site/uploads.html', {'documents': document_list})

	def post(self, request):
		form = DocumentForm(self.request.POST, self.request.FILES)
		if form.is_valid():
			document = request.user
	          	document = form.save()
		    	document.uploaded_at = timezone.now()
	            	data = {'is_valid': True, 'name': document.file.name, 'url': document.file.url}
		else:
		        data = {'is_valid': False}
		return JsonResponse({'message': 'Success'})
