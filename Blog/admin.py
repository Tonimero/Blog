from django.contrib import admin
from .models import *
# Register your models here.
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'description')
    prepopulated_fields = {"slug": ("title",)}  
    
class AdminCategory(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {"slug": ("title",)} 



# admin.site.register(Post)
admin.site.register(CategoryModel, AdminCategory)
admin.site.register(Post, AdminPost)