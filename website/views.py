from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm  


def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username='username',password = 'password')
        if user is not None:
            login(request,user)
            messages.success(request," You have been logged in successfully")
            return redirect('index')
        else:
            messages.success(request,"Something went wrong!! Please try again...")
            return redirect('index')
    else:
    
        return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request,username=username,password=password)

            login(request,user)
            messages.success(request,'you have been signed up....')
            return redirect('index')
    else:
        form = SignUpForm()
        return render(request, "signup.html", {'form':form})
    return render(request, "signup.html", {'form':form})


def login_user(request):
    pass
def logout_user(request):
    logout(request)
    messages.success(request," You have logged out...")
    return redirect('index')
    


# Create your views here.
