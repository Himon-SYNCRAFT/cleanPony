from cleanPony.core.actions import GetProduct, GetProductRequest
from cleanPony.core.entities import Product
from unittest.mock import Mock


def test_get_product():
    product_id = 1

    product_repository = Mock()
    product_repository.get.return_value = Product(id=product_id)

    request = GetProductRequest(product_id)
    action = GetProduct(product_repository)
    product = action.execute(request)

    assert product.id == product_id
