from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from typing import (Dict, Optional)
from cleanPony.core.entities import Location


class SaveLocation(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveLocationValidator()]

    def process(self, request: SaveLocationRequest) -> Location:
        location = Location.from_dict(request.to_dict())
        return self.repository.save(location)


@dataclass
class SaveLocationRequest(RequestBase):
    id: Optional[int]
    name: Optional[str]

    @staticmethod
    def from_dict(data: Dict) -> SaveLocationRequest:
        id = data.get("id", None)
        name = data.get("name", None)

        return SaveLocationRequest(
            id=id,
            name=name,
        )


class SaveLocationValidator(ValidatorBase):
    def _validate(self, request):
        pass
