from typing import Type
from cleanPony.core.entities import Entity
from cleanPony.db.models import Entity as Model
from cleanPony.db.repositories import CrudRepository
from cleanPony.core import repositories
from cleanPony.db import models
from cleanPony.core import entities


class InvalidEntity(Exception):
    pass


class Context:
    @staticmethod
    def get_repository(entity_cls: Type[Entity]) -> repositories.CrudRepository:
        model_cls = Context.get_model(entity_cls)
        return CrudRepository(model_cls=model_cls, entity_cls=entity_cls)

    @staticmethod
    def get_model(entity_cls: Type[Entity]) -> Type[Model]:
        if entity_cls == entities.Product:
            return models.Product
        elif entity_cls == entities.Title:
            return models.Title
        else:
            raise InvalidEntity(f'There is no model for {entity_cls}')
