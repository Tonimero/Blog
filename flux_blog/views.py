from django.shortcuts import render, get_object_or_404
from Blog.models import *

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'folders/index.html', context)