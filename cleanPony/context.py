from typing import Type

from cleanPony.core import entities
from cleanPony.core import repositories
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.entities import Entity
from cleanPony.core.exceptions import InvalidActionError, InvalidEntityError
from cleanPony.db import models
from cleanPony.db.models import Entity as Model


class Context:
    @staticmethod
    def get_repository(entity_cls: Type[Entity]) -> repositories.CrudRepository:
        from cleanPony.db.repositories import CrudRepository

        model_cls = Context.get_model(entity_cls)
        return CrudRepository(model_cls=model_cls, entity_cls=entity_cls)

    @staticmethod
    def get_model(entity_cls: Type[Entity]) -> Type[Model]:
        if entity_cls is entities.Product:
            return models.Product
        elif entity_cls is entities.Title:
            return models.Title
        elif entity_cls is entities.Location:
            return models.Location
        else:
            raise InvalidEntityError(f'There is no model for {entity_cls}')

    @staticmethod
    def get_action(action_cls: Type[ActionBase]) -> ActionBase:
        from cleanPony.core.actions.product.get_product import GetProduct
        from cleanPony.core.actions.product.find_products import FindProducts

        product_repository = Context.get_repository(entities.Product)

        if action_cls is GetProduct:
            return GetProduct(repository=product_repository)

        elif action_cls is FindProducts:
            return FindProducts(repository=product_repository)

        raise InvalidActionError(f'There is no action for {action_cls}')

    @staticmethod
    def get_mapper(entity_cls: Type[Entity]):
        from cleanPony.db.mappers.mapper_base import MapperBase
        model_cls = Context.get_model(entity_cls)
        return MapperBase(model_cls=model_cls, entity_cls=entity_cls)

