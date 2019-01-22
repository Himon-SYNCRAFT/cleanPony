from dataclasses import dataclass

from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.entities import Product
from cleanPony.core.validators.id_validator import IdValidator


@dataclass(frozen=True)
class GetProductRequest:
    id: int


class GetProduct(ActionBase):
    def __init__(self, product_repository: CrudRepository):
        super().__init__()
        self.product_repository = product_repository
        self._validators = [IdValidator()]

    def process(self, request: GetProductRequest) -> Product:
        return self.product_repository.get(request.id)
