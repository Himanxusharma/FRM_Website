from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    




    return render(request, "authentication/index.html")

def submit(request):

    if request.method == "post":
        #Acc = requst.POST.get('Acc')
        Acc = request.POST['Acc']
        Amt = request.POST['Amt']
        Pacc = request.POST['Pacc']

        myuser = User.objects.create_user(Acc, Amt, Pacc)

        # myuser.Acc = Acc
        # myuser.Amt = Amt
        # myuser.Pacc = Pacc

        myuser.save()

        messages.success(request, "Thanks, wait a while!")

        return redirect('submit')

    return render(request, "authentication/submit.html")


def signout(request):
    pass