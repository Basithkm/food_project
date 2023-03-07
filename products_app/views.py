from django.shortcuts import render
from django.http import HttpResponse
from  . models import Category,Product

# Create your views here.


def index(request):
    cate =Product.objects.all()
    return render(request,'index.html',{'category':cate})

def menu(request):
    cate =Category.objects.all()
    return render(request,'menu.html',{'category':cate})


def select_product(request,id):
    product=Product.objects.get(id=id)
    
    context ={
        'products':product
    }
    return render(request,'single_product.html',context)



def select_menu(request,id):
    cats=Category.objects.get(id=id)
    products =Product.objects.filter(category=cats)
    context ={
        'cat':cats,
        'products':products
    }
    return render(request,'products.html',context)

def offers(request):
    return render(request,'offers.html')

def hours(request):
    return render(request,'hours.html')


def contact(request):
    return render(request,'contact_me.html')



def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'register.html')

def cart(request):
    return render(request,'cart.html')


def checkout(request):
    return render(request,'checkout.html')