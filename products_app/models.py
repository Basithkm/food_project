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
    
class TableName(models.Model):
    table_name=models.CharField(max_length=200)



    def __str__(self) -> str:
        return self.table_name
    
STATUS_CHOICES={
    ('Pending','Pending'),
    ('Accepted','Accepted'),
    ('Deliverd','Deliverd')

}

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    amount =models.FloatField()
    razorpay_order_id =models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status =models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id =models.CharField(max_length=100,blank=True,null=True)
    paid =models.BooleanField(default=False)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    size = models.ForeignKey(ProductSizeAndPrice, on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=1,null=True)
    ordered_time=models.DateTimeField(auto_now_add=True)
    status =models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.size.price
