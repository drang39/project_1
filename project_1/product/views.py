from django.shortcuts import render,redirect

from django.http import HttpResponse

from django.db import connection
from .modeldb import Brand,Category,Product
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    
    if request.user.is_authenticated:
        
        
        pd = Product()
        columns = pd.column()
        datas = pd.all()
    


        return render(request,'product/index.html',locals())
    else :
        return render(request,'user/login.html')

def create(request):
    brand = Brand()
    datas = brand.all()
    category = Category()
    datas_category = category.all()

    if request.method =="POST":
       
    
        productname = request.POST['productname']
        productbrand = request.POST['productbrand']
        rating = request.POST['rating']
        productcategory = request.POST['productcategory']
        productprice = request.POST['productprice']
        
        description = request.POST['description']
        pd = Product()

        try:
            request.FILES['productimg']
            productimg = request.FILES['productimg']
            thefiles =  request.FILES['productimg']
            fs = FileSystemStorage()
            fs.save(thefiles.name,thefiles)
        except:
         productimg =''


        productinfo = tuple([productname,productbrand,rating,productcategory,productprice,productimg,description])
        pd.create(productinfo)
        return redirect('/product')



    return render(request,'product/create.html',locals())

def update(request):
    
    pid = int(request.POST['editid'])
    pd = Product()
    datas = pd.selectdata(pid)
    columns = pd.column()
    datasdict = {}
    brand = Brand()
    brands = brand.all()
    category = Category()
    categorys = category.all()
    for i in range(len(columns)):
        datasdict[columns[i][0]] = datas[i]
    
    print(datasdict)

    # productname = request.POST['productname']
    # productbrand = request.POST['productbrand']
    # rating = request.POST['rating']
    # productcategory = request.POST['productcategory']
    # productprice = request.POST['productprice']
    # productimg = request.FILES['productimg']
    # description = request.POST['description']


    # productinfo = tuple([productname,productbrand,rating,productcategory,productprice,productimg,description])
    # pd.update(productid,productinfo)
    return render(request,'product/update.html',locals())

def updatedb(request):
    pd = Product()
    productid = str(request.POST['productid'])
    productname = request.POST['productname']
    productbrand = request.POST['productbrand']
    rating = request.POST['rating']
    productcategory = request.POST['productcategory']
    productprice = request.POST['productprice']

    try:
        request.FILES['productimg']
        productimg = request.FILES['productimg']
        thefiles =  request.FILES['productimg']
        fs = FileSystemStorage()
        fs.save(thefiles.name,thefiles)
    except:
        productimg =''

    description = request.POST['description']
    productinfo = tuple([productname,productbrand,rating,productcategory,productprice,productimg,description,str(productid)])
    
    pd.update(productinfo)
   
        
    
    return redirect('/product')
def delete(request):
    pd = Product()
    did = request.POST['deleteid']
    pd.delete(did)
    return redirect('/product')