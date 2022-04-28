from django.shortcuts import render
from ecommerce.inventory import models

def home(request):
    return render(request, "index.html")

def category(request):
    
    data = models.Category.objects.all()

    return render(request, "categories.html", {"data": data})

def product_by_category(request, category):
    
    data = models.Product.objects.filter(category__name=category).values(
        "id", "name", "slug", "product__store_price", "category__name")

    return render(request, "product_by_category.html", {"data": data})

def product_detail(request, slug):

    data = models.ProductInventory.objects.filter(product__slug=slug).values(
        "id", "product__name", "store_price", "product_inventory__units",
        "attribute_values__attribute_value")


    return render(request, "product_detail.html", {"data": data})