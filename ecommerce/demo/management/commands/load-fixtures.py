from django.core.management import call_command
from django.core.management.base import BaseCommand


# python3 manage.py load-fixtures
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "db_admin_fixture.json")
        call_command("loaddata", "db_category_fixture.json")
        call_command("loaddata", "db_product_fixture.json")
        call_command("loaddata", "db_type_fixture.json")
        call_command("loaddata", "db_brand_fixture.json")
        call_command("loaddata", "db_product_inventory_fixture.json")
        call_command("loaddata", "db_media_fixture.json")
        call_command("loaddata", "db_stock_fixture.json")
        call_command("loaddata", "db_productattribute_fixture.json")
        call_command("loaddata", "db_productattributevalue_fixture.json")
        call_command("loaddata", "db_productattributevalues_fixture.json")