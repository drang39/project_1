from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    # return HttpResponse('<h2>hello</h2>')
    
    # name = request.GET['name']

    if request.user.is_authenticated:
        
        return render(request,'home/index.html',locals())
    

    
    return render(request,'home/index.html',locals())

def about(request):
    # return HttpResponse('<h2>about</h2>')
    css = '../../static/styles/about.css'
    return render(request,'home/about.html',locals())
def contact(request):
    css = '../../static/styles/contact.css'
    # return HttpResponse('<h2>contact</h2>')
    return render(request,'home/contact.html',locals())
def login(request):
    
        
    return render(request,'home/login.html',locals())
def signup(request):
  
    return render(request,'home/signup.html',locals())


def upload(request):
    if request.method =='POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fs.save(myfile.name,myfile)
        print(myfile.size)
    return render(request,'home/upload.html',locals())
