from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Person(AbstractUser):
    is_student = models.BooleanField(default=True)
    image = models.ImageField(upload_to='profile_image', null=True, blank=True, default='profile_image/default.png')

    def __unicode__(self):
        return u"{}".format(self.username)


class Slide(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __unicode__(self):
        return u"{}".format(self.name)


class Done(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Person, related_name='is_done')
    slide = models.ForeignKey(Slide, related_name='is_done', null=True, blank=True)

    def __unicode__(self):
        return u"{}, {}, {}".format(self.student, self.slide, self.date)


class Help(models.Model):
    helped = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Person, related_name='needs_help')
    slide = models.ForeignKey(Slide, related_name='needs_help', null=True, blank=True)

    def __unicode__(self):
        return u"{}, {}".format(self.student, self.date)


class Question(models.Model):
    answered = models.BooleanField(default=False)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Person, related_name='questions')
    slide = models.ForeignKey(Slide, related_name='questions', null=True, blank=True)

    def __unicode__(self):
        return u"{}, {}".format(self.student, self.date)


