from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.db import IntegrityError

# Create your views here.

def signup(request):
   
    users = User.objects.all()
    usernameli = []
    useremailli = []
    
    for user1 in users :
        usernameli.append(user1.username)
        useremailli.append(user1.email)
    print(usernameli)
    if request.user.is_authenticated :
        return redirect('/')
    if request.method == 'POST':
        userfirstname = request.POST["firstname"]
        userlastname = request.POST['lastname']
        password = request.POST["userpwd"]
        useremail = request.POST["email"]
        username = request.POST['username']
        warning = ""
        if useremail in useremailli:
            warning = 'useremail is already existed'
            
        if username in usernameli:
            warning += ' and username is already existed'
        if warning !="":
            return render(request,'user/signup.html',locals())
        else:
            try:
                user = User.objects.create_user(username,useremail,password)
                user.last_name = userlastname
                user.first_name = userfirstname
                user.save()
                login(request, user)
                return redirect('/')
            except IntegrityError:
                warning = 'something went wrong pls do it again'
                return render(request,'user/signup.html',locals())
    return render(request,'user/signup.html',locals())
def update(request):

    pass

def login_view(request):
    if request.user.is_authenticated :
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST["userpwd"]
        user = authenticate(username=username, password=password)
        if(user is not None):
            
            login(request, user)
            warning = 'login'
            name = user.username
            return render(request,'home/index.html',locals())
        else :
            
            warning = 'username or password is incorrect'
            
            render(request,'user/login.html',locals())

    return render(request,'user/login.html',locals())

def logout_view(request):
    logout(request)
    return render(request,'home/index.html')
