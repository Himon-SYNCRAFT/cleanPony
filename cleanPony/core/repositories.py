from typing import Generic, TypeVar, List
from cleanPony.core.filter import Filter


Entity = TypeVar('Entity')


class CrudRepository(Generic[Entity]):
    @staticmethod
    def get(entity_id: int) -> Entity:
        raise NotImplementedError

    @staticmethod
    def find(filters: List[Filter], page: int = 1, size: int = 10) -> List[Entity]:
        raise NotImplementedError

    @staticmethod
    def all() -> List[Entity]:
        raise NotImplementedError

    @staticmethod
    def save(entity: Entity) -> Entity:
        raise NotImplementedError
