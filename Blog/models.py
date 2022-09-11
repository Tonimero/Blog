from django.db import models
from django.urls import reverse


# Create your models here.


class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})

class Post(models.Model):
    STATUS = (
        ('PUBLISHED', 'PUBLISHED'),
        ('DRAF', 'DRAFT')
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=400, null=False, blank=False)
    intro = models.CharField(max_length=300)
    categories = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='categories')
    description = models.TextField()
    image = models.FileField(upload_to='static/images/blog_post_image', null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=100, default='PUBLISHED')
    published_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    
    class Meta:
        ordering = ('-published_at',)
        
    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE) #specifying a comment belonging to a particular post; getting all of the comment belonging to a post
    name = models.CharField(max_length=500)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name 

