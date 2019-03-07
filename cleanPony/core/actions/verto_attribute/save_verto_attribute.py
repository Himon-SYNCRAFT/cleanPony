from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from typing import (Dict, Optional)
from cleanPony.core.entities import (Product, VertoAttribute)


class SaveVertoAttribute(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveVertoAttributeValidator()]

    def process(self, request: SaveVertoAttributeRequest) -> VertoAttribute:
        verto_attribute = VertoAttribute.from_dict(request.to_dict())
        return self.repository.save(verto_attribute)


@dataclass
class SaveVertoAttributeRequest(RequestBase):
    id: Optional[int]
    product: Optional[Product]
    name: Optional[str]
    value: Optional[str]

    @staticmethod
    def from_dict(data: Dict) -> SaveVertoAttributeRequest:
        id = data.get("id", None)
        product = data.get("product", None)
        name = data.get("name", None)
        value = data.get("value", None)

        return SaveVertoAttributeRequest(
            id=id,
            product=product,
            name=name,
            value=value,
        )


class SaveVertoAttributeValidator(ValidatorBase):
    def _validate(self, request):
        pass
