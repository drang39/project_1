from django.shortcuts import render
from .models import *

from itertools import chain
# Create your views here.
def index(request):

    products = Product.objects.all()
    brands = Brand.objects.all()
    categorys = Category.objects.all()
    

    
    return render(request,'beer/index.html',locals())
def beerinfo(request,id):
    
    product = Product.objects.get(id=int(id))
    
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