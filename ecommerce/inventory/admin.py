from django.contrib import admin
from ecommerce.inventory.models import (
    Brand,
    Category,
    Product,
    ProductInventory,
    ProductType,
    Media,
)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductInventory)
admin.site.register(ProductType)
admin.site.register(Brand)
admin.site.register(Media)
