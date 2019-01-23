from cleanPony.db.models import db, Product, Title
from cleanPony.core.entities import Product as ProductEntity
from cleanPony.db.repositories import ProductRepository
from pony.orm import commit, db_session
from cleanPony.core.filter import Filter, FilterType

product_id = 1
product_name = 'product_name'
product_repository = ProductRepository()


def setup_function():
    db.create_tables()
    add_data()


def teardown_function():
    db.drop_all_tables(with_all_data=True)


@db_session
def add_data():
    product = Product(id=product_id, name=product_name)
    Title(id=1, name='title', product=product)
    commit()


def test_get_product():
    product = product_repository.get(entity_id=product_id)
    assert product.id == product_id
    assert type(product) is ProductEntity


def test_find_product():
    filters = {Filter(filter='name', value=product_name)}
    products = product_repository.find(filters=filters)
    assert products[0].name == product_name

    filter_value = 'name'
    filters = {Filter(filter='name', value=filter_value, operator=FilterType.LIKE)}
    products = product_repository.find(filters=filters)
    assert filter_value in products[0].name

