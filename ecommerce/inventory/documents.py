from pydoc import Doc
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import ProductInventory

@registry.register_document
class ProductInventoryDocument(Document):

    class Index:
        name = "productinventory"

    class Django:
        model = ProductInventory

        fields = ["id", "sku", ]