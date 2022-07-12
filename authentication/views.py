from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    # if request.method == "POST":
    #     Acc = request.POST.get('Acc')
    #     Amt = request.POST.get('Amt')
    #     Pacc = request.POST.get('Pacc')
    #     print(Acc)
    #     print(Amt)
    #     print(Pacc)



    #     # Acc = request.POST['Acc']
    #     # Amt = request.POST['Amt']
    #     # Pacc = request.POST['Pacc']
        
    #     myuser = User.objects.create_user(Acc, Amt, Pacc)

    #     # myuser.Acc = Acc
    #     # myuser.Amt = Amt
    #     # myuser.Pacc = Pacc

    #     myuser.save()

    #     messages.success(request, "Thanks, wait a while!")

    #     return redirect('submit')

    return render(request, "authentication/form.html")


def verify(request):


    Acc = request.GET["Acc"]
    Amt = request.GET["Amt"]
    Pacc = request.GET["Pacc"]

    return render(request, "authentication/submit.html",{ "Acc": Acc , "Amt": Amt , "Pacc": Pacc} )



# def submit(request):

#     return render(request, "authentication/submit.html")


# def signout(request):
#     pass