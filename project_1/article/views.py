from django.shortcuts import render,redirect

# Create your views here.
def index(request):


    return render(request,'article/index.html',locals())


def create(request):


    return render(request,'article/create.html',locals())



def update(request):


    return render(request,'article/update.html',locals())




def delte(request):


    return redirect('index/')