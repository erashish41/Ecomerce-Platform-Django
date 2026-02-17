from django.urls import path
from store.views import get_product_list

urlpatterns = [
    path("products/", get_product_list,name="product_list"),
    path("products/<slug:category_slug>/",get_product_list,name="product_by_category")
]
