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


# class EditPersonForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     class Meta:
#         model = Person
#         fields = ("username", "email", "password1", "password2", "image")
#
#     def clean_username(self):
#         # Since User.username is unique, this check is redundant,
#         # but it sets a nicer error message than the ORM. See #13147.
#         username = self.cleaned_data["username"]
#         try:
#             Person.objects.get(username=username)
#         except Person.DoesNotExist:
#             return username
#         raise forms.ValidationError(
#             self.error_messages['duplicate_username'],
#             code='duplicate_username',
#         )
#
#
# class TeacherForm(forms.Form):
#         date = forms.DateField(required=True)