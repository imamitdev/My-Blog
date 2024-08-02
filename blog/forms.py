from django import forms
from django.forms import ModelForm
from .models import Post, Category


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "post_image",
            "category",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.SelectMultiple(attrs={"class": "form-control"}),
            "post_image": forms.FileInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.all()
