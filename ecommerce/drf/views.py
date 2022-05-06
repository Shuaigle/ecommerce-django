from ecommerce.inventory.models import Product
from rest_framework import mixins, permissions, viewsets
from ecommerce.drf.serializer import AllProducts

class AllProductsViewsets(viewsets.ModelViewSet):

    queryset = Product.objects.all()[:10]
    serializer_class = AllProducts
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
