from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from slides.forms import PersonForm


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

# def edit_account(request):
#     if request.method == 'POST':
#         form = EditPersonForm(request.POST)
#         if form.is_valid():
#             date = request.POST['date']
#             print date
#             checks = Checked_in.objects.filter(date=date)
#             students = []
#             for check in checks:
#                 user = check.user.username
#                 if user not in students:
#                     students.append(user)
#             return render(request, "teacher_home.html", {'students': students, "date" : date})
#     else:
#         form = TeacherForm()
#
#     return render(request, "teacher_view.html", {'form': form})