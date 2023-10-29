from django.shortcuts import render
from .models import Products,Order,User
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password
# Create your views here.
def index(request):
    product_objects=Products.objects.all()
    
    #search code
    item_name=request.GET.get('item_name')
    if item_name!='' and item_name is not None:
        product_objects=Products.objects.filter(title__icontains=item_name)
    #paginator code
    paginator=Paginator(product_objects,8)
    page=request.GET.get('page')
    product_objects=paginator.get_page(page)
    return render(request,'shop/index.html',{'product_objects':product_objects})

def details(request,id):
    product_objects=Products.objects.get(id=id)
    return render(request,'shop/details.html',{'product_objects':product_objects})

def checkout(request):
    if request.method=="POST":
        item=request.POST.get("item",'')
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        address=request.POST.get("address","")
        land=request.POST.get("land","")
        mobile=request.POST.get("mobile","")
        emergency=request.POST.get("emergency","")
        city=request.POST.get("city","")
        state=request.POST.get("state","")
        zip=request.POST.get("zip","")
        total=request.POST.get("total","")
        order=Order(item=item,name=name,email=email,address=address,land=land,mobile=mobile,emergency=emergency,city=city,state=state,zip=zip,total=total)
        order.save()
        return render(request,'shop/orderplaced.html')
    return render(request,'shop/checkout.html')

def registorUser(request):
    if request.method=="POST":
        rq=request.POST
        name=rq.get("name","")
        email=rq.get("email",'')
        mobile=rq.get("mobile","")
        pass1=rq.get("pass1","")
        pass1=make_password(pass1)
        user=User(name=name,mobile=mobile,email=email,password=pass1)
        user.save()
        return render(request,'shop/login.html')
    return render(request,'shop/userRegistor.html')

def login(request):
    return render(request,'shop/login.html')
