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
def userinfo(request):

    if request.method =='POST':
        usn = request.POST['usn']
        u = User.objects.get(username=usn)
        u.email = request.POST['emailupdate']

        u.save()

    


    return render(request,'user/userinfo.html',locals())


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
            
            return render(request,'user/login.html',locals())

    return render(request,'user/login.html',locals())

def logout_view(request):
    logout(request)
    return render(request,'home/index.html')


def userinfoedit(request):
    return render(request,'user/userinfoedit.html')


def resetpwd(request):
    if request.method=='POST':
        password = request.POST['opwd']
        username= request.POST['username']

        u1 = authenticate(username=username,password=password)
        if u1 :
            u = User.objects.get(username=username)
            u.set_password(request.POST['npwd'])
            u.save()
            warning = 'pls use new password to login'
            return render(request,'user/login.html', {'warning': warning})
        else :
            return HttpResponse('password was wrong')
    return render(request,'user/resetpwd.html')