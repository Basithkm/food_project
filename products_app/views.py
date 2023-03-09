from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from  . models import Category,Product,ProductSizeAndPrice,CartItem
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.views import View
# Create your views here.





def index(request):
    if request.user.is_authenticated:
        cate =Category.objects.all()
        context={
            'category': cate,
            }
        return render(request,'index.html',context)
    
    else:
        return render(request,'login.html')


def galllery(request):
    if request.user.is_authenticated:
        cate=Product.objects.all()
        return render(request,'menu.html',{'category':cate})
    else:
        return render(request,'login.html')


def select_product(request,id):
    product=Product.objects.get(id=id)
    if request.user.is_authenticated:
        productssizeandprice=ProductSizeAndPrice.objects.filter(product=product)
        context ={
            'products':product,
            'productssizeandprice':productssizeandprice,
        }
        return render(request,'single_product.html',context)
    else:
        return render(request,'login.html')



def select_menu(request,id):
    cats=Category.objects.get(id=id)
    if request.user.is_authenticated:
        products =Product.objects.filter(category=cats)
        context ={
            'cat':cats,
            'products':products
        }
        return render(request,'products.html',context)
    else:
        return render(request,'login.html')

def offers(request):
    if request.user.is_authenticated:
        return render(request,'offers.html')
    else:
        return render(request,'login.html')

def hours(request):
    return render(request,'hours.html')


def contact(request):
    return render(request,'contact_me.html')



def login_page(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("password or userbname not currected")
    return render(request,'login.html')



def registration(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("password is not same")
        else:
            my_user =User.objects.create_user(uname,email,pass1)
            my_user.save()
        return redirect('index')
    return render(request,'register.html')

def logout_request(request):
    logout(request)
    return redirect('index')




def store(request):
    if request.user.is_authenticated:
        
        items=Product.objects.all()
        # context={'form': items,   
        #         }
        return render(request, 'offers.html')
    
    else:
        return render(request,'login.html')

# def cart(request):
#     user=request.user
#     size =request.GET('size')
#     print(size)
#     return redirect('/')


#  <a href="{% url 'checkout' %}" class="btn"><i class="fa-solid fa-bucket"></i>Orders</a> 

def add_to_cart_item(request, id):
    
    if request.user.is_authenticated:
        product = get_object_or_404(ProductSizeAndPrice, id=id)
        cart_item, created = CartItem.objects.get_or_create(
            size=product,
            user=request.user,
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect("/")
    else:
        return render(request,'login.html')
    

def add_to_cart(request, id):
    cart_item = get_object_or_404(CartItem, id=id,user=request.user)
    if request.user.is_authenticated:
        user=request.user
        cart_item.quantity += 1
        cart_item.save()
    
        return redirect("cart_detail")
    else:
        return redirect('login_page')
    

def remove_from_cart(request, id):
    cart_item = get_object_or_404(CartItem, id=id, user=request.user)
    if request.user.is_authenticated:
        user=request.user
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
        return redirect("cart_detail")
    else:
        return redirect('login_page')

def cart_detail(request):
    if request.user.is_authenticated:
        user=request.user
        cart_items = CartItem.objects.filter(user=request.user)
        total = sum(item.size.price * item.quantity for item in cart_items)
        return render(request, "cart.html", {
            "cart_items": cart_items,
            "total": total,
        })
    else:
        return redirect('login_page')

