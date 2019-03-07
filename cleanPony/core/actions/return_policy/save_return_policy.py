from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from typing import (Dict, Optional)
from cleanPony.core.entities import ReturnPolicy


class SaveReturnPolicy(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveReturnPolicyValidator()]

    def process(self, request: SaveReturnPolicyRequest) -> ReturnPolicy:
        return_policy = ReturnPolicy.from_dict(request.to_dict())
        return self.repository.save(return_policy)


@dataclass
class SaveReturnPolicyRequest(RequestBase):
    id: Optional[int]
    name: Optional[str]

    @staticmethod
    def from_dict(data: Dict) -> SaveReturnPolicyRequest:
        id = data.get("id", None)
        name = data.get("name", None)

        return SaveReturnPolicyRequest(
            id=id,
            name=name,
        )


class SaveReturnPolicyValidator(ValidatorBase):
    def _validate(self, request):
        pass
