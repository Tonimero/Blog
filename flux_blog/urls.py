from django.urls import path
from .views import *
from .models import *

urlpatterns = [
    path('', index, name='homepage')
]
