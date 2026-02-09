from django.contrib import admin
from category.models import Category, Product
from django.contrib.admin import ModelAdmin

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','description','category_type','is_active']
    list_filter = ['name','category_type','is_active']
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','description','category','price','is_active']
    list_filter = ['name','category','is_active','price']