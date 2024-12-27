from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import auth,User

# Create your views here.
def index(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        user=auth.authenticate(username=username,password=password,email=email)
        if user is not None:
            auth.login(request,user)
            return redirect(home)
        else:
            return redirect(index)
    return render(request,'index.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        data=User.objects.create_user(username=username,email=email,password=password)
        data.save()
        return redirect(index)
    return render(request,'register.html')

def home(request):
    if '_auth_user_id' in request.session:
        user=User.objects.get(pk=request.session['_auth_user_id'])
        return render(request,'home.html',{'user':user})
    else:
        return redirect(index)

def logout(request):
    if '_auth_user_id' in request.session:
        auth.logout(request)
        return redirect(index)

def upload_file(request):  
    if request.method == 'POST':  
        filename=request.FILES['file']
        data=files.objects.create(file=filename)
        data.save()
        return redirect(upload_file)
    return render(request,'home.html')
