from flask import request

from cleanPony.rest.app import app
from cleanPony.rest.helpers import json
from cleanPony.context import Context
from cleanPony.core.actions.product.get_product import GetProduct
from cleanPony.core.actions.product.find_products import FindProducts
from cleanPony.core.requests import FindRequest, IdRequest


@app.route('/api/product/<int:product_id>')
@json
def get_product(product_id):
    action = Context.get_action(GetProduct)
    return action.execute(IdRequest(id=product_id))


@app.route('/api/product/find', methods=['POST'])
@json
def find_products():
    action = Context.get_action(FindProducts)
    return action.execute(
        FindRequest.from_dict(request.json))
