from django.urls import path
from . import views

urlpatterns = [
    path("", views.posts, name="home"),
    path("create-post/", views.createPost, name="create-post"),
    path("post/<int:id>/", views.post_detail, name="post"),
]
