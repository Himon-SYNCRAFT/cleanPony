from typing import List, Set, TypeVar, Optional
from cleanPony.core.filter import Filter
from cleanPony.core.entities import Entity


E = TypeVar('E', bound=Entity)


class CrudRepository:
    def get(self, entity_id: int) -> E:
        raise NotImplementedError

    def get_or_none(self, entity_id: int) -> Optional[E]:
        raise NotImplementedError

    def find(self, filters: Set[Filter], page: int = 1, size: int = 10) -> List[E]:
        raise NotImplementedError

    def find_all(self, filters: Set[Filter]) -> List[E]:
        raise NotImplementedError

    def get_list(self, page: int = 1, page_size: int = 10) -> List[E]:
        raise NotImplementedError

    def get_all(self) -> List[E]:
        raise NotImplementedError

    def delete(self, entity_id: int) -> None:
        raise NotImplementedError

    def save(self, entity: E) -> E:
        raise NotImplementedError
