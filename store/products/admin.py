from django.contrib import admin
from .models import Product, ProductCategory
from .models import Restaurant, MenyCategory, Dish, Order


admin.site.register(Product)
admin.site.register(ProductCategory)

admin.site.register(Restaurant)
admin.site.register(MenyCategory)
admin.site.register(Dish)
admin.site.register(Order)
# Register your models here.
