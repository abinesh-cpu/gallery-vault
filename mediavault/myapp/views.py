from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        return redirect(home)
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        return redirect(index)
    return render(request,'register.html')

def home(request):
    return render(request,'home.html')

def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        return redirect(home)
    return render(request,'index.html')

def upload_file(request):  
    if request.method == 'POST':  
        filename=request.FILES['file']
        des=request.POST['des']
        data=files.objects.create(file=filename,description=des)
        data.save()
        return redirect(upload_file)
    return render(request,'home.html')
