# Generated by Django 4.1 on 2022-09-06 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=400)),
                ('intro', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.FileField(blank=True, null=True, upload_to='static/images/blog_post_image')),
                ('status', models.CharField(choices=[('PUBLISHED', 'PUBLISHED'), ('DRAF', 'DRAFT')], default='PUBLISHED', max_length=100)),
                ('published_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='Blog.categorymodel')),
            ],
            options={
                'ordering': ('-published_at',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='Blog.post')),
            ],
        ),
    ]
