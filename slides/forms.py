from django.contrib.auth.models import User

__author__ = 'j3dev'
import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from models import Person
from django.forms import ModelForm


class PersonForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Person
        fields = ["image", "username", "first_name", "last_name", "email", "password1", "password2"]

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Person.objects.get(username=username)
        except Person.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


class EditPersonForm(forms.Form):
    real_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'textb0x'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'textb0x'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'textb0x'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'textb0x'}))
    image = forms.ImageField()

    class Meta:
        model = Person
        fields = ["image", "email", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'textb0x'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'textb0x'}))

    class Meta:
        model = Person
        fields = ["username", "password1"]

    def clean_username(self):
        # Check for existing username
        username = self.cleaned_data["username"]
        try:
            Person.objects.get(username=username)
        except Person.DoesExist:
            return username
        raise forms.ValidationError(
            self.error_messages['username_does_not_exist'],
            code='username_does_not_exist',
        )

