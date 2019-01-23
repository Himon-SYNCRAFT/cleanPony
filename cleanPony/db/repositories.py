from typing import Type, Set, List, Optional
from pony.orm import db_session, flush

from cleanPony.core import repositories
from cleanPony.core.entities import Product
from cleanPony.core.filter import Filter, FilterType
from cleanPony.core.repositories import Entity
from cleanPony.db import models
from cleanPony.core.exceptions import NotFoundError


class CrudRepository(repositories.CrudRepository):
    def __init__(self, model_cls: Type[models.Entity], entity_cls: Type[Entity]) -> None:
        self._Entity = entity_cls
        self._Model = model_cls

    @db_session
    def get(self, entity_id: int) -> Entity:
        model = self._Model.get(id=entity_id)

        if model is None:
            raise NotFoundError(f'Not found {self._get_model_name()} with id {entity_id}')

        return self._model_to_entity(model)

    @db_session
    def get_or_none(self, entity_id: int) -> Optional[Entity]:
        model = self._Model.get(id=entity_id)

        if model is None:
            return None

        return self._model_to_entity(model)

    @db_session
    def find(self, filters: Optional[Set[Filter]] = None, page: Optional[int] = 1, page_size: Optional[int] = 10) -> List[Entity]:
        query = self._Model.select()

        if filters is not None:
            query = self._filter_query(query, filters)

        if page_size is not None and page is not None:
            query = query.page(page, page_size)

        return [self._model_to_entity(item) for item in list(query)]

    @db_session
    def find_all(self, filters: Set[Filter]) -> List[Entity]:
        return self.find(filters, page=None, page_size=None)

    @db_session
    def get_all(self) -> List[Entity]:
        return self.find(page=None, page_size=None)

    @db_session
    def get_list(self, page: int = 1, page_size: int = 10):
        return self.find(page=page, page_size=page_size)

    @db_session
    def save(self, entity: Entity) -> Entity:
        model = self._Model(**entity.to_dict())
        flush()
        return self._model_to_entity(model)

    @db_session
    def delete(self, entity_id: int) -> None:
        self._Model.get(id=entity_id).delete()

    def _model_to_entity(self, model: models.Entity):
        return self._Entity.from_dict(model.as_dict())

    def _get_model_name(self) -> str:
        return self._Model.__qualname__

    @staticmethod
    def _filter_query(query, filters: Set[Filter]):
        for f in filters:
            attribute, operator, value = f.filter, f.operator, f.value

            if operator == FilterType.EQ:
                query = query.filter(lambda e: getattr(e, attribute) == value)
            elif operator == FilterType.LT:
                query = query.filter(lambda e: getattr(e, attribute) < value)
            elif operator == FilterType.LE:
                query = query.filter(lambda e: getattr(e, attribute) <= value)
            elif operator == FilterType.NE:
                query = query.filter(lambda e: getattr(e, attribute) != value)
            elif operator == FilterType.GE:
                query = query.filter(lambda e: getattr(e, attribute) >= value)
            elif operator == FilterType.GT:
                query = query.filter(lambda e: getattr(e, attribute) > value)
            elif operator == FilterType.IN:
                query = query.filter(lambda e: getattr(e, attribute) in value)
            elif operator == FilterType.NOT_IN:
                query = query.filter(lambda e: getattr(e, attribute) not in value)
            elif operator == FilterType.LIKE:
                query = query.filter(lambda e: value in getattr(e, attribute))

        return query


class ProductRepository(CrudRepository):
    def __init__(self):
        super(ProductRepository, self).__init__(model_cls=models.Product, entity_cls=Product)
