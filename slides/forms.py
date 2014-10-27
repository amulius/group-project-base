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
        fields = ("username", "email", "password1", "password2", "image")

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
    email = forms.EmailField(required=True)
    real_name = forms.CharField(required=True)

    class Meta:
        model = Person
        fields = ("email", "password1", "password2", "image")

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

    def name_translation(self, real_name):
        names = real_name.split()
        username = self.Person.objects["username"]
        user = Person.objects.get(username=username)
        user.first_name = names[0]
        user.last_name = names[1]
        user.save()

#
#
# class TeacherForm(forms.Form):
#         date = forms.DateField(required=True)