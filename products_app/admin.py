from django.contrib import admin
from  . models import Category,Product,ProductSizeAndPrice,CartItem,TableName
# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductSizeAndPrice)
admin.site.register(CartItem)
admin.site.register(TableName)


# @admin.register(Cart)
# class CartModelAdmin(admin.ModelAdmin):
#     list_display=['id','user','product','size','price','quantity','total_cost']