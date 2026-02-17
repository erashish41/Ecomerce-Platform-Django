from django.contrib import admin
from category.models import Category
from django.contrib.admin import ModelAdmin

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name','slug','description','category_type','is_active']
    list_filter = ['name','category_type','is_active']
    
    
