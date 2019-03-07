from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from typing import (Dict, Optional)
from cleanPony.core.entities import Warranty


class SaveWarranty(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveWarrantyValidator()]

    def process(self, request: SaveWarrantyRequest) -> Warranty:
        warranty = Warranty.from_dict(request.to_dict())
        return self.repository.save(warranty)


@dataclass
class SaveWarrantyRequest(RequestBase):
    id: Optional[int]
    name: Optional[str]

    @staticmethod
    def from_dict(data: Dict) -> SaveWarrantyRequest:
        id = data.get("id", None)
        name = data.get("name", None)

        return SaveWarrantyRequest(
            id=id,
            name=name,
        )


class SaveWarrantyValidator(ValidatorBase):
    def _validate(self, request):
        pass
