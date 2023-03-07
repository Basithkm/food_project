from django.db import models

# Create your models here.



class Category(models.Model):
    category_name=models.CharField(max_length=255)
    category_image=models.ImageField(upload_to='category_image')

    def __str__(self) -> str:
        return self.category_name
    


class Product(models.Model):
    product_name =models.CharField(max_length=200)
    product_image =models.ImageField(upload_to='product_image')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product_name


class ProductSizeAndPrice(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    size =models.CharField(max_length=255)
    price =models.DecimalField(max_digits=6, decimal_places=2)


    



    