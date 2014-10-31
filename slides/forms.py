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
        fields = ("image", "username", "first_name", "last_name", "email", "password1", "password2")

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
    # email = forms.EmailField(required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'textb0x'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'textb0x'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'textb0x'}))
    image = forms.ImageField()

    class Meta:
        model = Person
        fields = ("real_name", "email", "password1", "password2", "image")


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


#
#
# class TeacherForm(forms.Form):
#         date = forms.DateField(required=True)