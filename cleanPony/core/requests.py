from __future__ import annotations
from typing import Dict, Set, List
from dataclasses import dataclass, field
from cleanPony.core.filter import Filter


class RequestBase:
    @staticmethod
    def from_dict(data: Dict) -> RequestBase:
        raise NotImplementedError


@dataclass(frozen=True)
class IdRequest(RequestBase):
    id: int

    @staticmethod
    def from_dict(data: Dict) -> IdRequest:
        id = data.get('id', None)
        return IdRequest(id)


@dataclass(frozen=True)
class PaginationRequest(RequestBase):
    page: int = 1
    page_size: int = 10

    @staticmethod
    def from_dict(data: Dict) -> PaginationRequest:
        page = data.get('page', 1)
        page_size = data.get('page_size', 10)

        return PaginationRequest(page=page, page_size=page_size)


@dataclass(frozen=True)
class FindRequest(PaginationRequest):
    filters: Set[Filter] = field(default_factory=set)

    @staticmethod
    def from_dict(data: Dict) -> FindRequest:
        result: Set[Filter] = set()
        filters: List[Dict] = data.get('filters', [])
        page = data.get('page', 1)
        page_size = data.get('page_size', 10)

        for f in filters:
            filter_name = f.get('filter', None)
            value = f.get('value', None)
            operator = f.get('operator', None)

            result.add(Filter(value, filter_name, operator))

        return FindRequest(filters=result, page=page, page_size=page_size)
