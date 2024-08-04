from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category
from .forms import PostForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required


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
        Q(category__name__icontains=q) | Q(title__icontains=q) | Q(content__icontains=q)
    )
    category = Category.objects.all()[0:5]

    context = {
        "posts": posts,
        "category": category,
    }
    return render(request, "home.html", context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "post/post_detail.html", {"post": post})


@login_required(login_url="login")
def createPost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()

            return redirect("home")
    else:
        form = PostForm()
    return render(request, "post/create-post.html", {"form": form})


@login_required
def post_list(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, "post/post_list.html", {"posts": posts})


@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():

            form.save()

            return redirect("post_list")
    else:
        form = PostForm(instance=post)
    return render(request, "post/create-post.html", {"form": form})


@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect("post_list")
    return render(request, "post/post_confirm_delete.html", {"post": post})
