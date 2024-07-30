from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Post, Category
from .forms import PostForm
from django.db.models import Q


# Create your views here.
def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    posts = Post.objects.filter(
        Q(category__name__icontains=q) | Q(title__icontains=q) | Q(content__icontains=q)
    )
    category = Category.objects.all()[0:5]

    context = {
        "posts": posts,
        "category": category,
    }
    return render(request, "home.html", context)


def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    posts = Post.objects.filter(
        Q(category__name__icontains=q)
        | Q(title__icontains=q)
        | Q(content__icontains=q)
    )
    category = Category.objects.all()[0:5]

    context = {
        "posts": posts,
        "category": category,
    }
    return render(request, "home.html", context)


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "post/post_detail.html", {"post": post})


def createPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()  # Save the many-to-many data for the form
            return redirect("home")  # Redirect to the desired URL after saving
    else:
        form = PostForm()
    return render(request, "post/create-post.html", {"form": form})


def topics(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    topics = Category.objects.filter(Q(name__icontains=q))
    context = {
        "topics": topics,
    }
    return render(request, "room/topics.html", context)
