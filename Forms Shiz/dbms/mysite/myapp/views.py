from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .models import Event,Admin,Payment,Customer,Booking
from .forms import *


# Create your views here.
def index(request):
    return render(request,'myapp/index.html')

def createEvent(request):
    return render(request,'myapp/createEvent.html')

def adminLogin(request):
    return render(request,'myapp/adminLogin.html')

def adminLobby(request):
    return render(request,'myapp/adminLobby.html')

def createAccount(request):
    return render(request,'myapp/createAccount.html')


def login(request):
    return render(request,'myapp/login.html')

def managerLogin(request):
    return render(request,'myapp/managerLogin.html')

# def signup(request):
#     print("Form is submitted")
#     #cus_id = request.POST["username"]
#     cus_contact = request.POST["cus_contact"]
#     cus_name =request.POST["cus_name"]
#     username =request.POST["username"]
#     password =request.POST["password"]
#     customer= Customer(cus_name=cus_name,cus_contact=cus_contact,username=username,password=password)
#     customer.save()
#     print("Helllloooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
#     return render(request,'myapp/createAccount.html')

def signup_view(request):
    if request.method =='POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            # login(request,username)
        context = {
            'form':form
        }

        return render (request,"myapp/createAccount.html",context)

    else:
        form = signupform(request.POST)
        context = {
                'form':form
            }
        return render (request,"myapp/createAccount.html",context)

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.get_user()
            login(request,username)
            context = {
            'form':form
            }

            return render (request,"myapp/createAccount.html",context)

    else:
        form = AuthenticationForm()
        context = {
                'form':form
            }
        return render (request,"myapp/login.html",context)

def event_view(request):
    if request.method =='POST':
        form = eventform(request.POST)
        if form.is_valid():
            form.save()

        context = {
            'form':form
        }
        print ("Hello")
        return render (request,"myapp/createEvent.html",context)

    else:
        form = eventform(request.POST)
        context = {
                'form':form
            }
        return render (request,"myapp/createEvent.html",context)
