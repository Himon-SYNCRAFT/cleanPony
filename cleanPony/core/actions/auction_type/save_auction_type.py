from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from typing import (Dict, Optional)
from cleanPony.core.entities import AuctionType


class SaveAuctionType(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveAuctionTypeValidator()]

    def process(self, request: SaveAuctionTypeRequest) -> AuctionType:
        auction_type = AuctionType.from_dict(request.to_dict())
        return self.repository.save(auction_type)


@dataclass
class SaveAuctionTypeRequest(RequestBase):
    id: Optional[int]
    name: Optional[str]

    @staticmethod
    def from_dict(data: Dict) -> SaveAuctionTypeRequest:
        id = data.get("id", None)
        name = data.get("name", None)

        return SaveAuctionTypeRequest(
            id=id,
            name=name,
        )


class SaveAuctionTypeValidator(ValidatorBase):
    def _validate(self, request):
        pass
