from django.shortcuts import render

# Create your views here.

def test_overlay(request):
    return render(request, "test_overlay.html")


def teacher(request):
    return render(request, "teacher.html")


def teacher_index(request):
    return render(request, "teacher_index.html")


def lecture(request, week_number, lecture_time):
    data = {
        'week_number': week_number,
        'lecture_time': lecture_time
    }
    return render(request, "lecture.html", data)

