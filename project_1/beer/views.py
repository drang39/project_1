from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from itertools import chain
from .forms import CommetForm
import datetime
from django.core import serializers
from collections import Counter

# Create your views here.
def index(request):
    if 'product_id_list' in request.session and 'product_q_list' in request.session:
        li = request.session['product_id_list']
        li1 = request.session['product_q_list']
        product_list = []
        for productid in li :
        
            product_list.append(Product.objects.filter(id=int(productid)))
        product_quantity_list = li1
  
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
  
        # products = serializers.serialize("json",products)

        p1 =  serializers.serialize("json", Product.objects.all())
        return HttpResponse(p1, content_type="application/json")

def beercartadd(request):
    
    pid = int(request.GET['pid'])
    # if request.user.is_authenticated:
        
    #     text = str(request.user.username+'productiL')
    #     text1 = str(request.user.username+'productqL')
    #     productiL = request.session[text]
    #     productqL = request.session[text1]
        
    #     if pid in productiL:
            
    #         productqL[productiL.index(pid)] = productqL[productiL.index(pid)]+1
    #         request.session[text1] = productqL

    #     else :

    #         productiL.append(pid)
    #         productqL.append(1)
    #         request.session[text] =productiL
    #         request.session[text1] =productqL 

    # else :
    
    if 'product_id_list' in request.session:
        
        if pid in request.session['product_id_list']:
            li = request.session['product_id_list']
            li1 = request.session['product_q_list']

            li1[li.index(pid)] = li1[li.index(pid)]+1
            request.session['product_id_list'] = li
            request.session['product_q_list'] = li1
            

        else:
        
            li = request.session['product_id_list']
            li1 = request.session['product_q_list']
            
            li.append(pid)
            li1.append(1)
            
            request.session['product_id_list'] = li
            request.session['product_q_list'] = li1
            
    else :

        li =[]
        li1 = []
        li.append(pid)
        li1.append(1)
        request.session['product_id_list'] = li
        request.session['product_q_list'] = li1
    
    return HttpResponse('/')
def cartshow(request):

    # if request.user.is_authenticated:
        
    #     text = str(request.user.username+'productiL')
    #     text1 = str(request.user.username+'productqL')
    #     li = request.session[text]
    #     li1 = request.session[text1]
    #     product_list = []
    #     for productid in li[1:] :
            
    #         product_list.append(Product.objects.filter(id=int(productid)))

    #         product_quantity_list = li1[1:]
            
    #     return render(request,'beer/cartshow.html',locals())



    # else:

    if 'product_id_list' in request.session and 'product_q_list' in request.session:
        li = request.session['product_id_list']
        li1 = request.session['product_q_list']
        product_list = []
        for productid in li :
        
            product_list.append(Product.objects.filter(id=int(productid)))
            product_quantity_list = li1
            
        return render(request,'beer/cartshow.html',locals())




    else :
        return HttpResponse('nothing in the cart')

    


def cartedit(request):

    if request.method =='GET':
        pid = int(request.GET['pid'])
        q  = int(request.GET['q'])
        li = request.session['product_id_list']
        li1 = request.session['product_q_list']
        
        location = li.index(pid)
        li1[location] = q
        
        request.session['product_id_list'] = li 
        request.session['product_q_list'] = li1
        
        return HttpResponse('/')
def cartdelete(request):
    
    if request.method =='GET':
        
        pid = int(request.GET['pid'])
        
        li = request.session['product_id_list']
        li1 = request.session['product_q_list']
        location = li.index(pid)
        li.pop(location)
        li1.pop(location)
        request.session['product_id_list'] = li 
        request.session['product_q_list'] = li1
        
        return HttpResponse('/')

def order(request):
    # if request.method =="GET":
    #     ol = request.GET['ol']

    #     print(ol)

    if request.method =='POST':
        li = request.session['product_id_list']
        li1 = request.session['product_q_list']
        amount = request.POST['amount']

        now = datetime.datetime.now()
        order = Order.objects.create(time = now, amount = amount ,user_id = (User.objects.get(id=(request.user.id)) if request.user.id else User.objects.get(id=(19))  ),product_id_list=li,product_quantity_list=li1)
        orders = Order.objects.filter(user_id = request.user.id)
        product_list =[]
        for productid in li :
        
            product_list.append(Product.objects.filter(id=int(productid)))
        request.session['product_id_list'] = []
        request.session['product_q_list'] = []
        return render(request,'beer/order.html',locals())
    else :
        orders = Order.objects.filter(user_id = request.user.id)
        product_order_list = []

        for order in orders:
            x = order.product_id_list
            
            li = x.replace('[',"").replace(']','').split(',')
            product_list = []
            
            for productid in li :
                
                product_list.append(Product.objects.filter(id=int(productid)))
            product_order_list.append(product_list)
            product_order_list.append(0)

        

        return render(request,'beer/order.html',locals())
def orderall(request):
    if request.user.is_staff:
        print(1)
        orders = Order.objects.all()
        return render(request,'beer/orderall.html',locals())
    else: 
        return render(request,'home/index.html')