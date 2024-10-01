from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts")
    banner = models.ImageField(default='fallback.png', blank=False)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


class Meeting(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="meets")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organiser")
    platform = models.CharField(max_length=200, unique=True)
    venue = models.CharField(max_length=200, unique=True)
    discription = models.TextField()
    start_time = models.DateTimeField()




