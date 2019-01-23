from __future__ import annotations
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.entities import Product
from dataclasses import dataclass, field
from typing import List, Set, Dict
from cleanPony.core.filter import Filter
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.request_base import RequestBase


@dataclass(frozen=True)
class FindProductsRequest(RequestBase):
    filters: Set[Filter] = field(default_factory=set)

    @staticmethod
    def from_dict(data: Dict) -> FindProductsRequest:
        result: Set[Filter] = set()
        filters: List[Dict] = data.get('filters', [])

        for f in filters:
            filter_name = f.get('filter', None)
            value = f.get('value', None)
            operator = f.get('operator', None)

            result.add(Filter(value, filter_name, operator))

        return FindProductsRequest(filters=result)


class FindProducts(ActionBase):
    def __init__(self, product_repository: CrudRepository):
        super().__init__()
        self.product_repository = product_repository

    def process(self, request: FindProductsRequest) -> List[Product]:
        return self.product_repository.find(request.filters)
