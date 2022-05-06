from rest_framework import serializers
from ecommerce.inventory.models import Product

class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description"]
        read_only = True
        editable = False
