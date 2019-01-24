from cleanPony.core.entities import Product
from decimal import Decimal


def test_product_from_dict():
    delivery = dict(id=1, name='test')
    images = [dict(id=1, url='http1'), dict(id=2, url='http2')]

    product_1 = dict(
        id=1,
        name='product',
        price=Decimal('1.23'),
        price_2=Decimal('2.23'),
        quantity=2,
        short_description='short',
        is_bundle=False,
        is_updated=True,
        delivery=delivery,
        attributes=[],
        auctions=[],
        bundle_items=[],
        categories=[],
        description=[],
        images=images,
        titles=[],
        verto_attributes=[],
    )

    Product.from_dict(product_1)
