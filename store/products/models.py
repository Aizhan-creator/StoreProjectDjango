from django.db import models


# Create your models here.
class ProductCategory(models.Model):
   name = models.CharField(max_length=128, unique=True)
   description = models.TextField(null=True, blank=True)

class Product(models.Model):
   name = models.CharField(max_length=256)
   description = models.TextField()
   price = models.DecimalField(max_digits=10, decimal_places=2)
   quantity = models.PositiveBigIntegerField(default=0)
   image = models.ImageField(upload_to='products_image')
   category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)




class Restaurant(models.Model):
   name = models.CharField(max_length=256)
   address = models.CharField(max_length=256)

class MenyCategory(models.Model):
   name = models.CharField(max_length=256)
   restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)

class Dish(models.Model):
   name = models.CharField(max_length=256)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   category = models.ForeignKey(to=MenyCategory, on_delete=models.CASCADE)

class Order(models.Model):
   client_name = models.CharField(max_length=256)
   date_ordered = models.DateField()
   restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)



