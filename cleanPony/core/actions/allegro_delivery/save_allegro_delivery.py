from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from cleanPony.core.entities import (Delivery, AllegroDelivery)
from typing import (Dict, Optional)


class SaveAllegroDelivery(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveAllegroDeliveryValidator()]

    def process(self, request: SaveAllegroDeliveryRequest) -> AllegroDelivery:
        allegro_delivery = AllegroDelivery.from_dict(request.to_dict())
        return self.repository.save(allegro_delivery)


@dataclass
class SaveAllegroDeliveryRequest(RequestBase):
    id: Optional[str]
    delivery_data: Delivery

    @staticmethod
    def from_dict(data: Dict) -> SaveAllegroDeliveryRequest:
        id = data.get("id", None)
        delivery_data = data.get("delivery_data", None)

        return SaveAllegroDeliveryRequest(
            id=id,
            delivery_data=delivery_data,
        )


class SaveAllegroDeliveryValidator(ValidatorBase):
    def _validate(self, request):
        pass
