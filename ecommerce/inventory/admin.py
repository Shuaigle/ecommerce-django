from django.contrib import admin
from ecommerce.inventory.models import (
    Brand,
    Category,
    Product,
    ProductInventory,
    ProductType,
    Media,
    Stock,
    ProductAttribute,
    ProductAttributeValue,
    ProductAttributeValues,
)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductInventory)
admin.site.register(ProductType)
admin.site.register(Brand)
admin.site.register(Media)
admin.site.register(Stock)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductAttributeValues)