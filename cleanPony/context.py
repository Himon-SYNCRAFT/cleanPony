from typing import Type

from cleanPony.core.entities import Entity
from cleanPony.db.models import Entity as Model
from cleanPony.db.repositories import CrudRepository
from cleanPony.core import repositories
from cleanPony.db import models
from cleanPony.core import entities
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.exceptions import InvalidActionError, InvalidEntityError


class Context:
    @staticmethod
    def get_repository(entity_cls: Type[Entity]) -> repositories.CrudRepository:
        model_cls = Context.get_model(entity_cls)
        return CrudRepository(model_cls=model_cls, entity_cls=entity_cls)

    @staticmethod
    def get_model(entity_cls: Type[Entity]) -> Type[Model]:
        if entity_cls is entities.Product:
            return models.Product
        elif entity_cls is entities.Title:
            return models.Title
        else:
            raise InvalidEntityError(f'There is no model for {entity_cls}')

    @staticmethod
    def get_action(action_cls: Type[ActionBase]) -> ActionBase:
        from cleanPony.core.actions.product.get_product import GetProduct
        from cleanPony.core.actions.product.find_products import FindProducts

        product_repository = Context.get_repository(entities.Product)

        if action_cls is GetProduct:
            return GetProduct(product_repository=product_repository)

        elif action_cls is FindProducts:
            return FindProducts(product_repository=product_repository)

        raise InvalidActionError(f'There is no action for {action_cls}')

