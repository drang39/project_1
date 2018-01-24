from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from itertools import chain
from .forms import CommetForm
import datetime
from django.core import serializers

# Create your views here.
def index(request):

    products = Product.objects.all()
    brands = Brand.objects.all()
    categorys = Category.objects.all()
    

    
    return render(request,'beer/index.html',locals())
def beerinfo(request,id):
    
    product = Product.objects.get(id=int(id))
    try:
        comments = Comment.objects.filter(product_id=int(id))
    except:
        pass
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

def beerinfocomment(request,id=None):
    if request.method =='POST':
        print(request.POST['fan'])
        form = CommetForm(request.POST)
        
        if form.is_valid():
            rating = request.POST['rating']
            comment = request.POST['comment']
          
          

            fan = request.POST['fan']
            now = datetime.datetime.now()
            comment = Comment.objects.create(time=now,fan = fan ,product_id = Product.objects.get(id=id) ,rating = rating,comment = comment, food = 'None',user_id =(User.objects.get(id=(request.user.id)) if request.user.id else User.objects.get(id=(19))  ))
            pid = str(comment.product_id.id)
            return redirect('../beerinfo/'+pid)
        else :
            return HttpResponse('something went wrong')
        
def beercommentedit(request,id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=int(id))
        comment.comment = request.POST['comment']
        comment.rating = request.POST['rating']
        comment.food = request.POST['food']
        comment.fan = request.POST['fan']
        comment.save()
        pid = str(comment.product_id.id)

        return redirect('../beerinfo/'+pid)
        
    else:
        comment = Comment.objects.get(id=int(id))
        
        return render(request,'beer/beerinfoedit.html',locals())
def beercommentdelete(request):
    if request.method =='POST':
        id = request.POST['act']
        comment = Comment.objects.get(id=id).delete()
        return redirect('/beer')
    return render(request,'beer/index.html')
def membercomment(request):
    uid = request.user.id

    comments = Comment.objects.filter(user_id=int(uid))

    return render(request,'beer/membercomment.html',locals())
def beersearch(request):

    if request.method =="POST":
        text = request.POST['searchtext']
        
        if Product.objects.filter(productname=text):
            product = Product.objects.filter(productname=text)
            
            product = product[0]
            try:
                comments = Comment.objects.filter(product_id=product.id)
            except:
                pass
           
            return render(request,'beer/beerinfo.html',locals()) 
        else :
            return HttpResponse('dont have any match')
def beersearchcontent(request):
    if request.method =='GET':
        products = Product.objects.values('productname')
        # products = serializers.serialize("json",products)

        p1 =  serializers.serialize("json", Product.objects.all())
        return HttpResponse(p1, content_type="application/json")











        # li = []
        # for i in products:
            
            
        #        li.append(i['productname'])
            
        
        # print(li)
        # print(products)
        # return JsonResponse(products,safe=False)
        # return JsonResponse({'products': list(products})
        # response = {}
        # response['product'] = serializers.serialize("json", Product.objects.all())
        # print(response)
        # return HttpResponse(response, content_type="application/json")

      