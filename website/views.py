from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm 
from.models import Record


def index(request):
    records = Record.objects.all()
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
    
        return render(request,'index.html',{'records':records})

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

def Customer_record(request,pk):
    if request.user.is_authenticated:
        Customer_record = Record.objects.get(id=pk)
        return render(request, 'records.html', {'Customer_record': Customer_record})
    else:
        messages.success(request,'You have to login first!!')
        return redirect('index')
    

def delete_record(request,pk):
        if request.user.is_authenticated:
            delete_it = Record.objects.get(id=pk)
            delete_it.delete()
            messages.success(request,'Record deleted successfully')
            return redirect('index')
        else:
            messages.success(request,'You must be logged in to delete record!!!')
            return redirect('index')
        
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('index')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('index')
def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('index')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('index')

    


# Create your views here.
