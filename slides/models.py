from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Person(AbstractUser):
    is_student = models.BooleanField(default=True)
    image = models.ImageField(upload_to='profile_image', null=True, blank=True, default='profile_image/default.png')

    def __unicode__(self):
        return u"{}".format(self.username)


class Done(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Person, related_name='is_done')

    def __unicode__(self):
        return u"{}, {}".format(self.student, self.date)


class Help(models.Model):
    helped = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Person, related_name='needs_help')

    def __unicode__(self):
        return u"{}, {}".format(self.student, self.date)


class Question(models.Model):
    answered = models.BooleanField(default=False)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Person, related_name='questions')

    def __unicode__(self):
        return u"{}, {}".format(self.student, self.date)


class Slide(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __unicode__(self):
        return u"{}".format(self.name)