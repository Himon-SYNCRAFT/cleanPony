from cleanPony.core.repositories import CrudRepository
from cleanPony.core.entities import Product
from dataclasses import dataclass, field
from typing import List, Set, Type
from cleanPony.core.filter import Filter
from cleanPony.core.actions.action_base import ActionBase


@dataclass(frozen=True)
class FindProductsRequest:
    filters: Set[Filter] = field(default_factory=set)


class FindProducts(ActionBase):
    def __init__(self, product_repository: Type[CrudRepository]):
        super().__init__()
        self.product_repository = product_repository

    def process(self, request: FindProductsRequest) -> List[Product]:
        return self.product_repository.find(request.filters)
