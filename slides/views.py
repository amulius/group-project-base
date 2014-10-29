import json
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from slides.forms import PersonForm, EditPersonForm
from slides.models import Person, Done, Slide, Help, Question


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


# @login_required
def edit_account(request):
    current_user = Person.objects.get(username=request.user)
    if request.method == 'POST':
        form = EditPersonForm(request.POST, request.FILES)
        if form.is_valid():
            real_name = request.POST["real_name"]
            email = request.POST["email"]
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]

            names = real_name.split()
            current_user = Person.objects.get(username=request.user)
            current_user.first_name = names[0]
            current_user.last_name = names[1]
            current_user.email = email
            current_user.password1 = password1
            current_user.password2 = password2
            current_user.save()

            return redirect("edit_account")
    else:
        form = EditPersonForm()

    return render(request, "edit_account.html", {'form': form, 'real_name': current_user.first_name + ' ' + current_user.last_name, 'email': current_user.email, 'password1': '', 'password2': ''})
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


@csrf_exempt
def student_actions(request):
    # print request
    if request.method == 'POST':
        data_in = json.loads(request.body)
        if data_in['action'] == 'done':
            print 'done'
            print data_in
            student = Person.objects.get(username=data_in['username'])
            slide, created = Slide.objects.get_or_create(name=data_in['slide'])
            Done.objects.create(student=student, slide=slide)
            data = {
                'return': 'good'
            }
        elif data_in['action'] == 'help':
            print 'help'
            print data_in
            student = Person.objects.get(username=data_in['username'])
            slide, created = Slide.objects.get_or_create(name=data_in['slide'])
            Help.objects.create(student=student, slide=slide)
            data = {
                'return': 'good'
            }
        elif data_in['action'] == 'submit_q':
            print 'submit_q'
            print data_in
            student = Person.objects.get(username=data_in['username'])
            slide, created = Slide.objects.get_or_create(name=data_in['slide'])
            Question.objects.create(student=student, slide=slide, text=data_in['question_text'])
            data = {
                'return': 'good'
            }
        return JsonResponse(data)