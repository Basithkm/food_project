from django.urls import path
from . import views
from .views import add_to_cart, remove_from_cart, cart_detail,add_to_cart_item


urlpatterns = [
    path('',views.index,name='index'),
    path('gallery',views.galllery,name='galllery'),
    path('menu/<int:id>/',views.select_menu,name='select_menu'),
    path('product/<int:id>/',views.select_product,name='select_product'),

    path('hours/',views.hours,name='hours'),
    path('contact/',views.contact,name='contact'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_request,name='logout_page'),
    path('register/',views.registration,name='register'),
    # path('add_to_cart/<int:id>/',views. add_to_cart, name='add_to_cart'),
    # path('cart/',views. cart, name='cart'),
    path("additem/<int:id>/", add_to_cart_item, name="add_to_cart_item"),
    path("add/<int:id>/", add_to_cart, name="add_to_cart"),
    path("remove/<int:id>/", remove_from_cart, name="remove_from_cart"),
    path("cart-details", cart_detail, name="cart_detail"),
]