from cleanPony.core.actions.product.find_products import FindProducts, FindProductsRequest
from unittest.mock import Mock
from cleanPony.core.entities import Product
from cleanPony.core.filter import Filter


def test_find_products():
    product_name = 'product_name'
    product_id = 1
    filters = {Filter(filter='name', value=product_name)}

    product_repository = Mock()
    product_repository.find.return_value = [Product(id=product_id, name=product_name)]

    request = FindProductsRequest(filters=filters)
    action = FindProducts(product_repository)
    product = action.execute(request).data[0]

    assert product['id'] == product_id
    assert product['name'] == product_name
