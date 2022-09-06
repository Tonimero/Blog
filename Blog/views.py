from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from .forms import CommentForm
from django.contrib import messages
from telnetlib import STATUS

# Create your views here.

# def base(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     posts = Post.objects.exclude(slug=slug)[:3]
#     categorys = CategoryModel.objects.all()
#     categories = CategoryModel.objects.all()
#     context = {
#         'posts':posts,
#         'categorys':categorys,
#         'post':post,
#         'posts': posts,
#         'categories':categories,
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