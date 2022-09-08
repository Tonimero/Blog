from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from telnetlib import STATUS
from django.utils.text import slugify

# Create your views here.

# def base(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     posts = Post.objects.exclude(slug=slug)[:3]
#     categorys = CategoryModel.objects.all()
#     context = {
#         'post':post,
#         'posts': posts,
#         'categorys':categorys
#     }
#     return render(request, 'folders/single-post.html', context)

def index(request):
    posts = Post.objects.all()
    categorys = CategoryModel.objects.all()
    context = {
        'posts':posts,
        'categorys':categorys,
    }
    return render(request, 'folders/index.html', context)


def postDetailPage(request, slug):
    post = get_object_or_404(Post, slug=slug)
    posts = Post.objects.exclude(slug=slug)[:3]
    categories = CategoryModel.objects.all()
    form = CommentForm 
    context = {
        'post':post,
        'posts': posts,
        'form': form,
        'categories':categories,
    }
    
    #form validation
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            #success message
            messages.success(request, ("Comment posted succesfully"))
            return redirect('post_details', slug=slug)
        else:
            messages.success(request, ("Please fill in the required information"))
            return redirect ('post_details', slug=slug)
    return render(request, 'folders/single-post.html', context)

def categoryListPages(request, slug):
    category = get_object_or_404(CategoryModel, slug=slug)
    posts = Post.objects.filter(categories=category)
    categorys = CategoryModel.objects.all()
    
    context = {
        'posts':posts, 
        'category':category,
        'categorys':categorys,
    }
    
    return render(request, 'folders/category.html', context)   


#Creating a "Create" form where users can create an article
def CreatePost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post =  form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            #success message
            messages.success(request, ("Comment posted succesfully"))
            return redirect ('homepage')
    context = {
            'form':form
        }
    return render(request, 'folders/create.html', context)

#updating the Create form

def  UpdatePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post) #form is filled with the particular article and not anither article
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect ('post_details', slug=post.slug)
    context = {
        'form':form,
        'post':post     
    }
    return render(request, 'folders/update.html', context)


#Delete the Create form
def DeletePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        post.delete()
        return redirect('homepage')
    context = {
        'form':form,
        'post':post 
    }
    return render(request, 'folders/delete.html', context)