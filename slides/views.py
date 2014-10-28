import json
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from slides.forms import PersonForm, EditPersonForm
from slides.models import Person



def test_overlay(request):

    return render(request, "test_overlay.html")

def register(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password1"]
            form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("slides_home")
    else:
        form = PersonForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

@login_required
def edit_account(request):
    if request.method == 'POST':
        form = EditPersonForm(request.POST, request.FILES)
        if form.is_valid():
            real_name = request.POST["real_name"]

            names = real_name.split()
            current_user = request.user
            current_user.first_name = names[0]
            current_user.last_name = names[1]
            current_user.save()

            return redirect("slides_home")
    else:
        form = EditPersonForm()

    return render(request, "edit_account.html", {'form': form})
    # person = Person.objects.get(id=person_id)
    # # We still check to see if we are submitting the form
    # if request.method == "POST":
    #     # We prefill the form by passing 'instance', which is the specific
    #     # object we are editing
    #     form = EditPersonForm(request.POST, request.FILES, instance=person)
    #     if form.is_valid():
    #         if form.save():
    #             return redirect("slides_home")
    # # Or just viewing the form
    # else:
    #     # We prefill the form by passing 'instance', which is the specific
    #     # object we are editing
    #     form = EditPersonForm(instance=person)
    # data = {"person": person, "form": form}
    # return render(request, "edit_account.html", data)

def teacher(request):
    return render(request, "teacher.html")


def done(request):
    return render(request, "done.html")


def help(request):
    return render(request, "help.html")


def question(request):
    return render(request, "question.html")


def teacher_index(request):
    return render(request, "teacher_index.html")


def lecture(request, week_number, lecture_time):
    data = {
        'week_number': week_number,
        'lecture_time': lecture_time
    }
    return render(request, "lecture.html", data)


@csrf_exempt
def lecture_fragment(request):
    if request.method == 'POST':
        data_in = json.loads(request.body)
        if data_in['want_lecture'] == 'yes':
            return render_to_response('lecture_fragment.html', data_in)


@csrf_exempt
def details(request):
    if request.method == 'POST':
        data_in = json.loads(request.body)
        if data_in['want'] == 'basic':
            return render_to_response('basic_info_fragment.html', data_in)