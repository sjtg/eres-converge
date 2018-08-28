# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.utils import timezone
from django.http import JsonResponse
from django.views import View
from .forms import *
from .models import *


# Home Page
def HomePage(request):
	return render(request, 'site/index.html', {})

#About us section
def Aboutus(request):
	return render(request, 'site/aboutus.html', {})

# Fees Section
def Fees(request):
	return render(request, 'site/fees.html', {})


#Dashboard Section
@login_required(login_url='login')
def Dashboard(request):
	DocumentList = Documents.objects.all()
    	return render(request, 'site/dashboard.html', {'new_doc': DocumentList})
	#return render(request, 'site/dashboard.html')

#Reviewer Section
@login_required(login_url='login')
def dashboard_reviewer(request):
	ReviewerList = Documents.objects.all()
    	return render(request, 'site/reviewer.html', {'review_doc': ReviewerList})

#Blog section
def PostList(request):
    PostLists = Post.objects.all().order_by('-PublishedDate')
    return render(request, 'site/board.html', {'PostLists': PostLists})

#Blog detail
def PostDetail(request, pk):
    PostDetails = get_object_or_404(Post, pk=pk)
    return render(request, 'site/post_detail.html', {'PostDetails': PostDetails})

#New Blog
@login_required(login_url='login')
def PostNew(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('PostDetail', pk=post.pk)
    else:
        form = PostForm(request.POST)
    return render(request, 'site/post_edit.html', {'form': form})

#Edit blog
@login_required(login_url='login')
def PostEdit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('PostDetail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'site/post_edit.html', {'form': form})





# New Document
@login_required
def NewDocs(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            new_doc = form.save()
            new_doc.user = request.user
            new_doc.published_date = timezone.now()
            new_doc.save()
            # return redirect('home',)
            return redirect('doc_detail', pk=new_doc.pk)
    else:
        form = DocumentsForm()
        # form = PostForm(request.POST, instance=new_post)
    return render(request, 'site/uploads.html', {'form' : form})

#Edit Document
@login_required(login_url='login')
def DocsEdit(request, pk):
    post = get_object_or_404(Documents, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            docs = form.save(commit=False)
            docs.author = request.user
            docs.published_date = timezone.now()
            docs.save()
            return redirect('docs_detail', pk=new_doc.pk)
    else:
        form = DocumentsForm(instance=post)
    return render(request, 'site/upload_edit.html', {'form': form})


@login_required
def ReviewerDocs(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            review_doc = form.save()
            review_doc.user = request.user
            review_doc.published_date = timezone.now()
            review_doc.save()
            # return redirect('home',)
            return redirect('review_detail', pk=review_doc.pk)
    else:
        form = ResearchForm()
        # form = PostForm(request.POST, instance=new_post)
    return render(request, 'site/uploads.html', {'form' : form})



# class UploadView(View):
#     	def get(self, request):
# 	        document_list = Document.objects.all()
# 	        return render(self.request, 'site/uploads.html', {'documents': document_list})
#
# 	def post(self, request):
# 		form = DocumentForm(self.request.POST, self.request.FILES)
# 		if form.is_valid():
# 			document = request.user
# 	          	document = form.save()
# 		    	document.uploaded_at = timezone.now()
# 	            	data = {'is_valid': True, 'name': document.file.name, 'url': document.file.url}
# 		else:
# 		        data = {'is_valid': False}
# 		return JsonResponse({'message': 'Success'})
