from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Category(models.Model):
    category_name=models.CharField(max_length=255)
    category_image=models.ImageField(upload_to='category_image')

    def __str__(self) -> str:
        return self.category_name
    


class Product(models.Model):
    product_name =models.CharField(max_length=200,null=True)
    product_image =models.ImageField(upload_to='product_image',null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    product_description =models.TextField(null=True)

    def __str__(self) -> str:
        return self.product_name


class ProductSizeAndPrice(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    size =models.CharField(max_length=255)
    price =models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self) -> str:
        return self.size




# class Cart(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     size=models.ForeignKey(ProductSizeAndPrice,on_delete=models.CASCADE)

# class CartItem(models.Model):
#     cart =models.ForeignKey(Cart,on_delete=models.CASCADE)
#     product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
#     size=models.ForeignKey(ProductSizeAndPrice,on_delete=models.CASCADE)
#     quantity=models.PositiveIntegerField(default=1)

#     @property
#     def price(self):
#         return self.size.price

#     @property
#     def total_cost(self):
#         return self.quantity * self.size.price


class CartItem(models.Model):
    size = models.ForeignKey(ProductSizeAndPrice, on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=1,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    @property
    def price(self):
        return self.size.price
    
    @property
    def total_cost(self):
        return self.quantity * self.size.price

    def __str__(self):
        return f"{self.quantity} of {self.size.product.product_name}"