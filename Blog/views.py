from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from .forms import CommentForm
from django.contrib import messages
from telnetlib import STATUS

# Create your views here.

def index(request):
    posts = Post.objects.order_by('-published_at') 
    context = {
        'posts':posts,
    }
    return render(request, 'folders/index.html', context)


def postDetailPage(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories = CategoryModel.objects.all()
    form = CommentForm
    context = {
        'post':post,
        'form': form,
        'categories':categories
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
            return redirect('single-post', slug=slug)
        else:
            messages.success(request, ("Please fill in the required information"))
            return redirect ('post_detail', slug=slug)
    return render(request, 'folders/single-post.html', context)

def categoryListPages(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories=category)
    
    return render(request, 'folders/category.html', {'posts':posts, 'category':category})