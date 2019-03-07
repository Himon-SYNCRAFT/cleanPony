from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from builtins import float
from typing import (Dict, Optional)
from cleanPony.core.entities import (DeliveryOptionType, DeliveryOptionValue)


class SaveDeliveryOptionValue(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveDeliveryOptionValueValidator()]

    def process(self, request: SaveDeliveryOptionValueRequest) -> DeliveryOptionValue:
        delivery_option_value = DeliveryOptionValue.from_dict(request.to_dict())
        return self.repository.save(delivery_option_value)


@dataclass
class SaveDeliveryOptionValueRequest(RequestBase):
    id: Optional[int]
    delivery_option_type: Optional[DeliveryOptionType]
    first_piece_cost: float
    next_pieces_cost: float
    quantity: int

    @staticmethod
    def from_dict(data: Dict) -> SaveDeliveryOptionValueRequest:
        id = data.get("id", None)
        delivery_option_type = data.get("delivery_option_type", None)
        first_piece_cost = data.get("first_piece_cost", None)
        next_pieces_cost = data.get("next_pieces_cost", None)
        quantity = data.get("quantity", None)

        return SaveDeliveryOptionValueRequest(
            id=id,
            delivery_option_type=delivery_option_type,
            first_piece_cost=first_piece_cost,
            next_pieces_cost=next_pieces_cost,
            quantity=quantity,
        )


class SaveDeliveryOptionValueValidator(ValidatorBase):
    def _validate(self, request):
        pass
