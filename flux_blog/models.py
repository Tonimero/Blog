from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, null=False, blank=False)
    intro = models.CharField(max_length=500)
    description = models.TextField()
    image = models.FileField(upload_to='static/imag/blog_post_image', null=True, blank=True)
    status = (
        ('PUB', 'PUBLISHED'),
        ('DRAF', 'DRAFT')
    )
    post_status = models.CharField(choices=status, max_length=50, default='PUBLISHED')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
