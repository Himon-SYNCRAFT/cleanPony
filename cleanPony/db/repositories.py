from typing import List, Type, Optional
from cleanPony.core import repositories
from cleanPony.core.entities import Product
from cleanPony.core.filter import Filter
from cleanPony.core.repositories import Entity
from cleanPony.db import models
from pony.orm import db_session, flush
from operator import eq


class CrudRepository(repositories.CrudRepository):
    def __init__(self, model: Type[models.Entity], entity_type: Type[Entity]) -> None:
        self._entity_type = entity_type
        self._model = model

    @db_session
    def get(self, entity_id: int) -> Entity:
        model = self._model.get(id=entity_id)
        return self._entity_type(**model.to_dict())

    @db_session
    def find(self, filters: List[Filter], page: int = 1, page_size: int = 10) -> List[Entity]:
        query = self._model.select()

        for f in filters:
            filter, operator, value = f.filter, f.operator, f.value

            if operator == 'eq':
                query = query.filter(lambda e: getattr(e, filter) == value)
            elif operator == 'lt':
                query = query.filter(lambda e: getattr(e, filter) < value)
            elif operator == 'le':
                query = query.filter(lambda e: getattr(e, filter) <= value)
            elif operator == 'ne':
                query = query.filter(lambda e: getattr(e, filter) != value)
            elif operator == 'ge':
                query = query.filter(lambda e: getattr(e, filter) >= value)
            elif operator == 'gt':
                query = query.filter(lambda e: getattr(e, filter) > value)
            elif operator == 'in':
                query = query.filter(lambda e: getattr(e, filter) in value)
            elif operator == 'notin':
                query = query.filter(lambda e: getattr(e, filter) not in value)
            elif operator == 'like':
                query = query.filter(lambda e: getattr(e, filter) in value)

        return list(query)

    @db_session
    def all(self) -> List[Entity]:
        return list(self._model.select())

    @db_session
    def save(self, entity: Entity) -> Entity:
        model = self._model(**entity.asdict())
        flush()
        return model


class ProductRepository(CrudRepository):
    def __init__(self):
        super(ProductRepository, self).__init__(model=models.Product, entity_type=Product)
