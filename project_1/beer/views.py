from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from itertools import chain
from .forms import CommetForm
# Create your views here.
def index(request):

    products = Product.objects.all()
    brands = Brand.objects.all()
    categorys = Category.objects.all()
    

    
    return render(request,'beer/index.html',locals())
def beerinfo(request,id):
    
    product = Product.objects.get(id=int(id))
    comments = Comment.objects.filter(product_id=3)
    print(comments)
    return render(request,'beer/beerinfo.html',locals())
# def seleted_index(request,id):
#     products = Product.objects.filter(brand_id = id)
#     brands = Brand.objects.all()
#     categorys = Category.objects.all()
    
#     if len(products)>0 :

#         print(123)
#         return render(request,'beer/index.html',locals())
#     else :
#         products = Product.objects.all()
#         return render(request,'beer/index.html',locals()) 

def beerinfocomment(request,id):
    if request.method =='POST':
        form = CommetForm(request.POST)
        
        if form.is_valid():
            rating = request.POST['rating']
            comment = request.POST['comment']
            food = request.POST['food']
            

            fan = request.POST['fan']
            comment = Comment.objects.create(fan = fan ,product_id = Product.objects.get(id=id) ,rating = rating,comment = comment, food = food,user_id =User.objects.get(id=(request.user.id)))
            return HttpResponse('good')
        else :
            return HttpResponse('something went wrong')
def beerinfoedit(request,id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=int(id))
        comment.comment = request.POST['comment']
        comment.rating = request.POST['rating']
        comment.food = request.POST['food']
        comment.fan = request.POST['fan']
        comment.save()
        pid = str(comment.product_id.id)
        # product = Product.objects.get(id=int(id))
        # comments = Comment.objects.filter(product_id=pid)
        return redirect('../beerinfo/'+pid)
        
    else:
        comment = Comment.objects.get(id=int(id))
        return render(request,'beer/beerinfoedit.html',locals())
def beerinfodelte(request):
    if request.method =='POST':
        id = request.POST['act']
        comment = Comment.objects.get(id=id).delete()
        return render(request,'beer/index.html',locals())
    return render(request,'beer/index.html')