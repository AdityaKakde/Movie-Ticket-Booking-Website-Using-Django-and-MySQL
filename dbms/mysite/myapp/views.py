from django.shortcuts import render

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
