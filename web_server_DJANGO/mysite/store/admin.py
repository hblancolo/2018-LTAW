from django.contrib import admin

from .models import Product, BuyOrder

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','product_type', 'pub_date')

admin.site.register(Product, ProductAdmin)
admin.site.register(BuyOrder)