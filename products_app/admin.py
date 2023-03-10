from django.contrib import admin
from  . models import Category,Product,ProductSizeAndPrice,CartItem,TableName
# Register your models here.


# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(ProductSizeAndPrice)
# admin.site.register(CartItem)
# admin.site.register(TableName)


# @admin.register(Cart)
# class CartModelAdmin(admin.ModelAdmin):
#     list_display=['id','user','product','size','price','quantity','total_cost']



@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display=['id','category_name','category_image']



@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','product_name','product_image','category','product_description']


@admin.register(ProductSizeAndPrice)
class ProductSizeAndPriceModelAdmin(admin.ModelAdmin):
    list_display=['id','product','size','price']


@admin.register(CartItem)
class CartItemModelAdmin(admin.ModelAdmin):
    list_display=['id','product','size','quantity','user']


@admin.register(TableName)
class TableNameModelAdmin(admin.ModelAdmin):
    list_display=['id','table_name']
