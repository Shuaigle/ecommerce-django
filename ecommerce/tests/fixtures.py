import pytest
from django.contrib.auth.models import User
from django.core.management import call_command

# @pytest.fixture
# def create_admin_user(django_user_model):
#     return django_user_model.objects.create_superuser("admin", "admin@a.com", "admin")


@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    Load contents into test database
    and remove databases after the test run
    """
    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixture.json")
        call_command("loaddata", "db_category_fixture.json")
        call_command("loaddata", "db_product_fixture.json")
        call_command("loaddata", "db_type_fixture.json")
        call_command("loaddata", "db_brand_fixture.json")
        call_command("loaddata", "db_product_inventory_fixture.json")
        
