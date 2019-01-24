from unittest.mock import Mock

from cleanPony.core.actions.product.get_product import GetProduct
from cleanPony.core.entities import Product
from cleanPony.core.requests import IdRequest


def test_get_product():
    product_id = 1

    product_repository = Mock()
    product_repository.get.return_value = Product(id=product_id)

    request = IdRequest(product_id)
    action = GetProduct(product_repository)
    product = action.execute(request).data

    assert product['id'] == product_id
