from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name='index'),
    path('menu/',views.menu,name='menu'),
    path('menu/<int:id>/',views.select_menu,name='select_menu'),
    path('product/<int:id>/',views.select_product,name='select_product'),
    path('offers/',views.offers,name='offers'),
    path('hours/',views.hours,name='hours'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('register/',views.registration,name='register'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
]
