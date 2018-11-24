from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import (authenticate,get_user_model,logout)
from django.contrib.auth import login as log
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib.auth.models import User

customer = get_user_model
# Create your views here.
def index(request):
    return render(request,'myapp/index.html')

def createEvent(request):
    return render(request,'myapp/createEvent.html')

def eventScreen(request):
    return render(request,'myapp/eventScreen.html')

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
        form = signupform()
        context = {
            'form':form
        }

        return render (request,"myapp/createAccount.html",context)

    else:
        form = signupform()
        context = {
                'form':form
            }
        return render (request,"myapp/createAccount.html",context)

def login_view(request):
        if request.method =='POST':
            print('view 1')
            form = loginform(request.POST or None)
            if form.is_valid():
                print('view 2')
                username= form.cleaned_data.get('username')
                password= form.cleaned_data.get('password')
                user= authenticate(username=username,password=password)
                print(user)
                if user:
                    print(user)
                    log(request,user)
                    print(request.user.is_authenticated())

            context = {
                    'form':form
                }
            return render (request,"myapp/login.html",context)
        else:
            form = loginform()
            context = {
                    'form':form
                }
            return render (request,"myapp/login.html",context)





# def login_view(request):
#     if request.method =='POST':
#         user = request.POST['username']
#         pas = request.POST['password']
#         try:
#             user = auth.authenticate(username=username,password=password)
#             if user is not None:
#                 auth.login(request,user)
#                 return render (request,eventScreen)
#
#
#             return render (request,"myapp/createAccount.html",context)
#
#     else:
#         form = AuthenticationForm()
#         context = {
#                 'form':form
#             }
#         return render (request,"myapp/login.html",context)

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
