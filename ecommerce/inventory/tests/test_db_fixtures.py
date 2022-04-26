import pytest
from django.db import IntegrityError
from ecommerce.inventory import models
from decimal import Decimal

@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "skirt", "skirt", 1),
        (2, "maxdress", "maxdress", 1),
    ],
)
def test_inventory_category_dbfixture(
    db, db_fixture_setup, id, name, slug, is_active
):
    result = models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize(
    "slug, is_active",
    [
        ("skirt", 1),
        ("maxdress", 1),
    ],
)
def test_inventory_category_insert_data(db, category_factory, slug, is_active):
    """
    fatories.py generated fake data for pytest
    """
    result = category_factory.create(slug=slug, is_active=is_active)
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, web_id, name, slug, description, is_active, created_at, updated_at",
    [
        (
            1,
            "00114444",
            "jojokeyboard",
            "keyboard_114444",
            "Black Switches - If you’re into fast-paced games such as first-person shooters, linear switches will give you an edge. There is no dome to compress or click to overcome, the keystroke is consistent and smooth that offers unmistakable feedback when pressed.",
            1,
            "2022-04-19T05:24:35",
            "2022-04-19T05:24:35",
        ),
        (
            2,
            "00437777",
            "Taydey A-Line Pleated Vintage Skirts for Women",
            "skir-437777",
            "The print on the dress (if any) might be slightly different from pictures for different batch productions\r\nPlease don't soak the dress in water for a long time, otherwise the dye will fade(Of course,dye won't fade under normal washing)",
            1,
            "2022-04-19T05:26:31",
            "2022-04-19T05:26:31",
        ),
    ],
)
def test_inventory_product_dbfixture(
    db,
    db_fixture_setup,
    id,
    web_id,
    name,
    slug,
    description,
    is_active,
    created_at,
    updated_at,
):
    result = models.Product.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%dT%H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%dT%H:%M:%S")
    assert result.web_id == web_id
    assert result.name == name
    assert result.slug == slug
    assert result.description == description
    assert result.is_active == is_active
    assert result_created_at == created_at
    assert result_updated_at == updated_at


def test_inventory_product_uniqueness_integrity(db, product_factory):
    # create -> create -> raises
    new_web_id = product_factory.create(web_id=123456789)
    with pytest.raises(IntegrityError):
        product_factory.create(web_id=123456789)


@pytest.mark.dbfixture
def test_inventory_product_insert_data(db, product_factory):
    new_product = product_factory.create(category=(1, 2, 3, 4))
    # print(new_product.category.all())
    result_product_category = new_product.category.all().count()
    assert "web_id_" in new_product.web_id
    assert result_product_category == 4


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, sku, upc, product_type, product, brand, is_active, retail_price, store_price, sale_price, weight, created_at, updated_at",
    [
        (
            1,
            "1111111",
            "123123",
            1,
            1,
            "shuaigle",
            1,
            '97.00',
            '92.00',
            '44.00',
            724,
            "2022-04-21 08:34:09",
            "2022-04-21 08:34:09",
        ),
        (
            5,
            "1235436",
            "2445674",
            1,
            1,
            "shuaigle",
            1,
            '92.00',
            '111.11',
            '41.00',
            721,
            "2022-04-21 08:37:30",
            "2022-04-21 08:37:30",
        ),
    ],
)
def test_inventory_product_inventory_dbfixture(
    db,
    db_fixture_setup,
    id,
    sku,
    upc,
    product_type,
    product,
    brand,
    is_active,
    retail_price,
    store_price,
    sale_price,
    weight,
    created_at,
    updated_at,
):
    result = models.ProductInventory.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    assert result.sku == sku
    assert result.upc == upc
    assert product_type == product_type
    assert result.brand.name == brand
    assert result.store_price == Decimal(store_price)   # warning asserst Decimal == float
    assert result_created_at == created_at


def test_inventory_product_inventory_insert_data(
    db, product_inventory_factory
):
    new_product = product_inventory_factory.create(
        sku="11112211",
        upc="314235y946375",
        product_type__name="new_name",
        product__web_id="11111122",
        brand__name="new_name",
    )
    assert new_product.sku == "11112211"

def test_inventory_producttype_insert_data(db, product_type_factory):
    new_type = product_type_factory.create(name="demo_type")
    assert new_type.name == "demo_type"

def test_inventory_db_producttype_uniqueness_integrity(db, product_type_factory):
    product_type_factory.create(name="is_unique")
    with pytest.raises(IntegrityError):
        product_type_factory.create(name="is_unique")

def test_inventory_brand_insert_data(db, brand_factory):
    new_brand = brand_factory.create(name="new_brand")
    assert new_brand.name == "new_brand"

@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, product_inventory, image, alt_text, is_feature, created_at, updated_at",
    [
        (
            1,
            1,
            "images/default.png",
            "black",
            1,
            "2022-04-26 02-20-51",
            "2022-04-26 02-20-51",
        ),
        (
            4,
            4,
            "images/default.png",
            "pink",
            1,
            "2022-04-26 02-23-07",
            "2022-04-26 02-23-07",
        ),
    ],
)
def test_inventory_media_dbfixture(
    db,
    db_fixture_setup,
    id,
    product_inventory,
    image,
    alt_text,
    is_feature,
    created_at,
    updated_at,
):
    result = models.Media.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H-%M-%S")
    assert result.product_inventory.id == product_inventory
    assert result.image == image
    assert result.alt_text == alt_text
    assert result_created_at == created_at

def test_inventory_media_insert_data(db, media_factory):
    new_media = media_factory.create(product_inventory__sku="123123123")
    assert new_media.product_inventory.sku == "123123123"