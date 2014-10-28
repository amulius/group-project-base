from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from slides.forms import PersonForm, EditPersonForm
from slides.models import Person


def test_overlay(request):

    return render(request, "test_overlay.html")

def register(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password1"]
            form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("home")
    else:
        form = PersonForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


def edit_account(request):
    if request.method == 'POST':
        form = EditPersonForm(request.POST)
        if form.is_valid():
            real_name = request.POST["real_name"]

            # names = real_name.split()
            # username = self.Person.objects["username"]
            # user = Person.objects.get(username=username)
            # user.first_name = names[0]
            # user.last_name = names[1]
            # user.save()

            return redirect("slides_home")
    else:
        form = EditPersonForm()

    return render(request, "edit_account.html", {'form': form})


def teacher(request):
    return render(request, "teacher.html")

def done(request):
    return render(request, "done.html")

def help(request):
    return render(request, "help.html")

def question(request):
    return render(request, "question.html")
