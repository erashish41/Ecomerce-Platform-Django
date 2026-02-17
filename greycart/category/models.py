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