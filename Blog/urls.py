from .views import *
from .models import *
from django.urls import path

urlpatterns = [
    path('post/<slug:slug>/', blog_post, name='single-post'),
    path('category/<slug:slug>/', category_details, name='category')
]
