from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts")
    banner = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | Posted by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class Meeting(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="meets")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organiser")
    platform = models.CharField(max_length=200, unique=True)
    venue = models.CharField(max_length=200, unique=True)
    discription = models.TextField()
    start_time = models.DateTimeField()

    class Meta:
        ordering = ["-start_time"]

    def __str__(self):
        return f"Meeting {self.discription} created by {self.author}"


