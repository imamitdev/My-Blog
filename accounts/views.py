from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import RegistrationFrom, UserProfileForm, UserForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import User, UserProfile
from blog.models import Post, Category

# Create your views here.


def user_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "login successful!")
            return redirect("home")

        else:
            messages.error(request, "something went wrong")
            return redirect("login")
    return render(request, "login.html")


def user_register(request):
    if request.method == "POST":
        print(request.POST)
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            username = email.split("@")[0]
            user = User.objects.create_user(
                name=name,
                email=email,
                username=username,
                password=password,
            )
            user.save()

            profile = UserProfile()
            profile.user_id = user.id
            profile.profile_picture = "default-user.png"
            profile.save()
            messages.success(request, "Registration successful!")
            return redirect("login")
    else:
        form = RegistrationFrom()
    context = {"form": form}
    return render(request, "register.html", context)


@login_required(login_url="login")
def user_logout(request):
    auth.logout(request)
    messages.success(request, "You are Logged out")
    return redirect("login")


def user_profile(request, username):
    user = User.objects.get(username=username)
    user_profile = get_object_or_404(UserProfile, user=user)
    posts = Post.objects.filter(author=user)

    context = {
        "user_profile": user_profile,
        "posts": posts,
    }
    return render(request, "user_profile.html", context)


@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        # Handle the profile update
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=user_profile
        )
        # Handle the user update
        user_form = UserForm(request.POST, instance=request.user)

        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, "update successful!")

            return redirect("profile")
    else:
        profile_form = UserProfileForm(instance=user_profile)
        user_form = UserForm(instance=request.user)

    return render(
        request,
        "profile-edit.html",
        {
            "profile_form": profile_form,
            "user_form": user_form,
            "user_profile": user_profile,
        },
    )
