from django.contrib import admin
from .models import *
# Register your models here.
class AdminPost(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  
    
class AdminCategory(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)} 



# admin.site.register(Post)
admin.site.register(CategoryModel, AdminCategory)
admin.site.register(Post, AdminPost)
admin.site.register(Comment)