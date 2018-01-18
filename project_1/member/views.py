from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import datetime
from .models import Member
from django.core import serializers
# Create your views here.
def index(request):  
    
    title = "會員管理"
    members = Member.objects.all()
    #todo 讀取會員資料傳給index.html
    
    return render(request,'member/index.html',locals())

def create(request):
    

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        useremail = request.POST["useremail"]
        userbirth = request.POST["userbirth"]
      
        
        #todo 接收到的會員資料寫進資料庫
        
        #todo 新增完成後轉到http://localhost:8000/member
        return redirect('/member')
    title = "會員新增" 
    return render(request,'member/create.html',locals())

def update(request,id):
    if request.method == 'POST':        
        username = request.POST["username"]      
        useremail = request.POST["useremail"]
        userbirth = request.POST["userbirth"]

        #todo 修改資料庫中的會員資料
        member = Member.objects.get(id=int(id))
        member.username = username
        member.useremail = useremail
        member.userbirth = userbirth
        member.save()
        #todo 修改完成後轉到http://localhost:8000/member
        return redirect('/member')
    title = "會員修改"

    member = Member.objects.get(id=int(id))


def valid(request):
    members = Member.objects.all()
    datas = serializers.serialize('json',members)
    return JsonResponse(datas,safe=False)




    #todo 根據會員編號取得會員資料傳給update.html
    
    return render(request,'member/update.html',locals())

def delete(request,id):
    #todo 根據會員編號刪除會員資料
    member = Member.objects.get(id=int(id))
    member.delete()
    #todo 刪除完成後轉到http://localhost:8000/member
    return redirect('/member')

def login(request):    
    if request.method =='POST':
        email = request.POST['useremail']
        pwd = request.POST['userpassword']
        member = Member.objects.filter(useremail=email,password=pwd).values('username')
        if member:
            themember = member[0]
            
            response = HttpResponse('<script>alert("ok")</script>')
            if 'rememberme' in request.POST.keys() and request.POST['rememberme']:
                expiredate = datetime.datetime.now() + date.timedelta(day=7)
                response.set_cookie('name',themember['username'], expires = expiresdate)
            else:
                response.set_cookie('name',themember['username'])
            return response
        else :
            return HttpResponse('<script>alert("not ok")</script>')

    title = "會員登入"
    return render(request,'member/login.html',locals())

def logout(request):
    response = HttpResponse('<script>alert("log out")</script>')
    response.delete_cookie('name')
    return response
