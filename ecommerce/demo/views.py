from django.shortcuts import render
from ecommerce.inventory import models
from django.db.models import Count
from django.contrib.postgres.aggregates import ArrayAgg


def home(request):
    return render(request, "index.html")


def category(request):
    
    data = models.Category.objects.all()

    return render(request, "categories.html", {"data": data})


def product_by_category(request, category):
    
    data = models.Product.objects.filter(category__name=category).filter(
        product__is_default=True).values(
        "id", "name", "slug", "created_at", "category__name", "product__store_price")

    return render(request, "product_by_category.html", {"data": data})


def product_detail(request, slug):

    filter_arguments = []

    if request.GET:
        for value in request.GET.values():
            filter_arguments.append(value)

        data = models.ProductInventory.objects.filter(product__slug=slug).filter(
            attribute_values__attribute_value__in=filter_arguments).annotate(
            num_tags=Count('attribute_values')).filter(num_tags=len(filter_arguments)
            ).values(
            "id", "sku", "product__name", "store_price", "product_inventory__units"
            ).annotate(field_a=ArrayAgg("attribute_values__attribute_value")).get()

        # print(data)
        
    else:
        data = models.ProductInventory.objects.filter(product__slug=slug).filter(
            is_default=True).values(
            "id", "sku", "product__name", "store_price", "product_inventory__units"
            ).annotate(field_a=ArrayAgg("attribute_values__attribute_value")).get()
        
        # print(data)

    att_val_name = models.ProductInventory.objects.filter(product__slug=slug
        ).distinct().values(
        "attribute_values__product_attribute__name", "attribute_values__attribute_value")

    att_name = models.ProductTypeAttribute.objects.filter(
        product_type__product_type__product__slug=slug).distinct().values(
        "product_attribute__name")
 
    return render(request, "product_detail.html", 
                {"data": data, "att_val_name": att_val_name,"att_name": att_name})