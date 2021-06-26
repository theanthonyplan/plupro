from django.contrib import admin
from products.models import Product
# Register your models here.

class ProductTabularInline(admin.TabularInline):
    model = Product
    extra = 1



class ProductAdmin(admin.ModelAdmin):
    model = Product
    # list_display = ['quantity', 'category','override','proposal']


admin.site.register(Product, ProductAdmin)
