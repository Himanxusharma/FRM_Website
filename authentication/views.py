from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "authentication/index.html")

def submit(request):
    return render(request, "authentication/submit.html")


def signout(request):
    pass