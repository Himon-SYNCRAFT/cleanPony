from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from typing import (Dict, Optional)
from cleanPony.core.entities import ImpliedWarranty


class SaveImpliedWarranty(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveImpliedWarrantyValidator()]

    def process(self, request: SaveImpliedWarrantyRequest) -> ImpliedWarranty:
        implied_warranty = ImpliedWarranty.from_dict(request.to_dict())
        return self.repository.save(implied_warranty)


@dataclass
class SaveImpliedWarrantyRequest(RequestBase):
    id: Optional[int]
    name: Optional[str]

    @staticmethod
    def from_dict(data: Dict) -> SaveImpliedWarrantyRequest:
        id = data.get("id", None)
        name = data.get("name", None)

        return SaveImpliedWarrantyRequest(
            id=id,
            name=name,
        )


class SaveImpliedWarrantyValidator(ValidatorBase):
    def _validate(self, request):
        pass
