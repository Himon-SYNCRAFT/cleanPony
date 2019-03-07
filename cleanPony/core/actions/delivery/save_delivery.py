from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from typing import (List, Dict, Optional)
from cleanPony.core.entities import (Delivery, DeliveryOptionValue)


class SaveDelivery(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveDeliveryValidator()]

    def process(self, request: SaveDeliveryRequest) -> Delivery:
        delivery = Delivery.from_dict(request.to_dict())
        return self.repository.save(delivery)


@dataclass
class SaveDeliveryRequest(RequestBase):
    id: Optional[int]
    name: Optional[str]
    is_updated: bool
    options: List[DeliveryOptionValue]

    @staticmethod
    def from_dict(data: Dict) -> SaveDeliveryRequest:
        id = data.get("id", None)
        name = data.get("name", None)
        is_updated = data.get("is_updated", None)
        options = data.get("options", None)

        return SaveDeliveryRequest(
            id=id,
            name=name,
            is_updated=is_updated,
            options=options,
        )


class SaveDeliveryValidator(ValidatorBase):
    def _validate(self, request):
        pass
