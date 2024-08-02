from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationFrom
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from .models import User, UserProfile

# Create your views here.


def user_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
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


def user_profile(request):
    return render(request, "user_profile.html")
