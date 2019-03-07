from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from typing import (Dict, Optional)
from cleanPony.core.entities import DescriptionItemType


class SaveDescriptionItemType(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveDescriptionItemTypeValidator()]

    def process(self, request: SaveDescriptionItemTypeRequest) -> DescriptionItemType:
        description_item_type = DescriptionItemType.from_dict(request.to_dict())
        return self.repository.save(description_item_type)


@dataclass
class SaveDescriptionItemTypeRequest(RequestBase):
    id: Optional[int]
    name: Optional[str]

    @staticmethod
    def from_dict(data: Dict) -> SaveDescriptionItemTypeRequest:
        id = data.get("id", None)
        name = data.get("name", None)

        return SaveDescriptionItemTypeRequest(
            id=id,
            name=name,
        )


class SaveDescriptionItemTypeValidator(ValidatorBase):
    def _validate(self, request):
        pass
