from django.shortcuts import render

# Create your views here.

def test_overlay(request):
    return render(request, "test_overlay.html")
