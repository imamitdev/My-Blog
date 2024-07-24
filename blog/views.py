from django.shortcuts import render, HttpResponse, redirect
from .models import Post


# Create your views here.
def posts(request):
    posts = Post.objects.all()
    context = {"blogs": posts}
    return render(request, "home.html", context)
