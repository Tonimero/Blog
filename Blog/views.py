from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import CommentForm
from django.contrib import messages

# Create your views here.
def blog_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm
    context = {
        'post':post,
        'form': form
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
            return redirect ('blog-post', slug=slug)
    return render(request, 'folders/single-post.html', context)

def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories=category) #filtering the post model and assigning the categories from models.py to the category variable created 
    context = {
        'category':category,
        'posts':posts
    }
    
    return render(request, 'folders/category.html', context)