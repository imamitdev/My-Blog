from typing import Any, Dict
from .models import User, UserProfile
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class RegistrationFrom(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter Password", "class": "form-control"}
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter Password", "class": "form-control"}
        )
    )

    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "password",
        ]

    def __init__(self, *args, **kwargs):
        super(RegistrationFrom, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["placeholder"] = "Enter First Name"
        self.fields["email"].widget.attrs["placeholder"] = "Enter Email Address"
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"

    def clean(self):
        cleaned_data = super(RegistrationFrom, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password does not match !")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "name",
        ]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class UserProfileForm(forms.ModelForm):
    avatar = forms.ImageField(
        required=False,
        error_messages={"invalid": ("image files only")},
        widget=forms.FileInput,
    )

    class Meta:
        model = UserProfile
        fields = [
            "bio",
            "address",
            "avatar",
        ]

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "name",
        ]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
