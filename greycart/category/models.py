from django.db import models
from utils.models import BaseMixin
from cloudinary.models import CloudinaryField

# Create your models here.

CATEGORY_TYPE = (
    ('cloth', 'Cloth'),
    ('shoe', 'Shoe'),
    ('utils', 'Utils'),
    ('jewelry', 'Jewelry'),
    ('electronic', 'Electronic'),
    ('furniture', 'Furniture'),
    ('sports', 'Sports'),
)

class Category(BaseMixin):
    name = models.CharField(max_length=150,unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)
    category_type = models.CharField(choices=CATEGORY_TYPE, max_length=20)
    image = CloudinaryField('image', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ["name"]
    
    def __str__(self):
        return self.name
    
    
class Product(BaseMixin):
    name = models.CharField(max_length=150,unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    manufacture_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = CloudinaryField('image',blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ["name"]
        
    def __str__(self):
        return self.name
    