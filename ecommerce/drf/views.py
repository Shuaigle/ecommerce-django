from ecommerce.drf import serializer
from ecommerce.inventory.models import Product
from rest_framework import mixins, permissions, viewsets
from ecommerce.drf.serializer import AllProducts
from rest_framework.response import Response

class AllProductsViewsets(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):

    queryset = Product.objects.all()
    serializer_class = AllProducts
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        """
        Use slug for queries
        """
        queryset = Product.objects.filter(category__slug=slug)
        serializer = AllProducts(queryset, many=True)
        return Response(serializer.data)