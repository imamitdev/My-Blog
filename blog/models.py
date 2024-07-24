from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category


class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(max_length=500)
    published_date = models.DateTimeField(auto_now=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
