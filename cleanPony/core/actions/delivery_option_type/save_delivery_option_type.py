from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from typing import (Dict, Optional)
from cleanPony.core.entities import DeliveryOptionType


class SaveDeliveryOptionType(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveDeliveryOptionTypeValidator()]

    def process(self, request: SaveDeliveryOptionTypeRequest) -> DeliveryOptionType:
        delivery_option_type = DeliveryOptionType.from_dict(request.to_dict())
        return self.repository.save(delivery_option_type)


@dataclass
class SaveDeliveryOptionTypeRequest(RequestBase):
    id: Optional[int]
    name: Optional[str]
    is_active: bool

    @staticmethod
    def from_dict(data: Dict) -> SaveDeliveryOptionTypeRequest:
        id = data.get("id", None)
        name = data.get("name", None)
        is_active = data.get("is_active", None)

        return SaveDeliveryOptionTypeRequest(
            id=id,
            name=name,
            is_active=is_active,
        )


class SaveDeliveryOptionTypeValidator(ValidatorBase):
    def _validate(self, request):
        pass
