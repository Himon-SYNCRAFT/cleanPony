from cleanPony.core.repositories import CrudRepository
from cleanPony.core.entities import Product
from dataclasses import dataclass, field
from typing import List
from cleanPony.core.filter import Filter


@dataclass(frozen=True)
class GetProductRequest:
    id: int


class GetProduct:
    def __init__(self, product_repository: CrudRepository):
        self.product_repository = product_repository

    def execute(self, request: GetProductRequest) -> Product:
        return self.product_repository.get(request.id)


@dataclass(frozen=True)
class FindProductsRequest:
    filters: List[Filter] = field(default_factory=list)


class FindProducts:
    def __init__(self, product_repository: CrudRepository):
        self.product_repository = product_repository

    def execute(self, request: FindProductsRequest) -> List[Product]:
        return self.product_repository.find(request.filters)
