import json
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from slides.forms import PersonForm, EditPersonForm, LoginForm
from slides.models import Person, Done, Slide, Help, Question


def test_overlay(request):
    return render(request, "test_overlay.html")


def student_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
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
        form = LoginForm()

    return render(request, "includes/login.html", {
        'form': form,
    })


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
        print form
        print request.POST
        print request.FILES
        if form.is_valid():
            real_name = request.POST["real_name"]
            email = request.POST["email"]
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]
            print form
            names = real_name.split()
            current_user = Person.objects.get(username=request.user)
            if len(request.FILES):
                image = request.FILES["file1"]
                current_user.image = image
            current_user.first_name = names[0]
            current_user.last_name = names[1]
            current_user.email = email
            current_user.password1 = password1
            current_user.password2 = password2
            current_user.save()

            return redirect("edit_account")
    else:
        current_user = Person.objects.get(username=request.user)
        data = {
            'image': current_user.image,
            'real_name': current_user.first_name + ' ' + current_user.last_name,
            'email': current_user.email,
            'password1': '',
            'password2': ''
        }
        form = EditPersonForm(initial=data)

    return render(request, "edit_account.html", {'form': form, })


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


def done_test(request, week_number, lecture_time):
    data = {
        'week_number': week_number,
        'lecture_time': lecture_time
    }
    return render(request, "done_body_fragment.html", data)


def help_test(request, week_number, lecture_time):
    data = {
        'week_number': week_number,
        'lecture_time': lecture_time
    }
    return render(request, "help_body_fragment.html", data)


def question_test(request, week_number, lecture_time):
    data = {
        'week_number': week_number,
        'lecture_time': lecture_time
    }
    return render(request, "question_body_fragment.html", data)


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
        slide = Slide.objects.filter(name=data_in['slide'])
        if data_in['want'] == 'basic':
            if slide:
                data = {
                    'slide': data_in['slide'],
                    'done': Done.objects.filter(slide=slide[0]).distinct('student').count(),
                    'help': Help.objects.filter(slide=slide[0], helped=False).count(),
                    'question': Question.objects.filter(slide=slide[0], answered=False).count(),
                }
            else:
                data = {
                    'slide': data_in['slide'],
                    'done': 0,
                    'help': 0,
                    'question': 0,
                }
            return render_to_response('basic_info_fragment.html', data)
        elif data_in['want'] == 'done':
            # print 'done'
            # print slide
            if slide:
                data = {
                    'done_count': Done.objects.filter(slide=slide[0]).distinct('student').count(),
                    'dones': Done.objects.filter(slide=slide[0]).distinct('student'),
                    'not_dones': Person.objects.filter(is_student=True).exclude(is_done__slide=slide[0])
                }
            else:
                data = {
                    'done_count': 0,
                    'dones': 0,
                    'not_dones': Person.objects.filter(is_student=True)
                }
            # print data
            return render_to_response('done_info_fragment.html', data)
        elif data_in['want'] == 'help':
            if slide:
                data = {
                    'help_count': Help.objects.filter(slide=slide[0], helped=False).count(),
                    'helps': Help.objects.filter(slide=slide[0]).order_by('date'),
                }
            else:
                data = {
                    'help_count': 0,
                    'help': 0,
                }
            return render_to_response('help_info_fragment.html', data)
        elif data_in['want'] == 'question':
            if slide:
                data = {
                    'question_count': Question.objects.filter(slide=slide[0], answered=False).count(),
                    'questions': Question.objects.filter(slide=slide[0]).order_by('date'),
                }
            else:
                data = {
                    'question_count': 0,
                    'questions': 0,
                }
            return render_to_response('question_info_fragment.html', data)


@csrf_exempt
def update(request):
    if request.method == 'POST':
        data_in = json.loads(request.body)
        print data_in
        pk = data_in['pk']
        if data_in['want'] == 'helped':
            active_help = Help.objects.get(pk=pk)
            print active_help
            active_help.helped = True
            active_help.save()
            data = {
                'updated': pk
            }
            return JsonResponse(data)
        elif data_in['want'] == 'answered':
            active_question = Question.objects.get(pk=pk)
            active_question.answered = True
            active_question.save()
            data = {
                'updated': pk
            }
            return JsonResponse(data)


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




