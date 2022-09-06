from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    # path('post/<slug:slug>/', base, name='base'),
    path('post/<slug:slug>/', postDetailPage, name='post_details'),
    path('category/<slug:slug>/', categoryListPages, name='category_detail'),
]
 