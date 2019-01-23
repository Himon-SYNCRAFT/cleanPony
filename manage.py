from pony.orm import commit, db_session

from cleanPony.rest.app import app
from cleanPony.db.models import db, Product, Title


@db_session
def add_data():
    product = Product(id=1, name='product_name')
    Title(id=1, name='title', product=product)
    commit()
    print('created')


if __name__ == '__main__':
    db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
    db.generate_mapping(create_tables=True)
    db.create_tables()
    app.run(debug=True)
