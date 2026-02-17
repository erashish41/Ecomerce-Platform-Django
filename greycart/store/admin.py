from django.contrib import admin
from store.models import Product
from django.contrib.admin import ModelAdmin

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name','category','price', 'stock' ,'is_available']
    list_filter = ['name','category','is_available','price']