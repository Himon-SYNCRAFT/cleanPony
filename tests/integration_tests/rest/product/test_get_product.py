from cleanPony.db.models import db, Product, Title
from cleanPony.db.repositories import CrudRepository
from cleanPony.core.entities import Product as ProductEntity
from pony.orm import commit, db_session
from flask.json import loads


product_id = 1
product_name = 'product_name'
product_repository = CrudRepository(Product, ProductEntity)


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


def test_get_product(client):
    response = client.get(f'/api/product/{product_id}')
    result = loads(response.data)
    print(result)

    assert result['id'] == product_id


def test_get_not_existing_product(client):
    response = client.get(f'/api/product/{9}')
    result = loads(response.data)

    errors = result['errors']
    assert len(errors) > 0
