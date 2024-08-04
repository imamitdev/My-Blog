from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.post_list, name="post_list"),
    path("create-post/", views.createPost, name="create-post"),
    path("posts/<slug:slug>/edit/", views.post_edit, name="post_edit"),
    path("posts/<slug:slug>/delete/", views.post_delete, name="post_delete"),
    path("post/<slug:slug>/", views.post_detail, name="post"),
]
