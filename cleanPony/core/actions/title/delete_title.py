from __future__ import annotations
from dataclasses import dataclass
from typing import Dict

from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validators.id_validator import IdValidator
from cleanPony.core.request_base import RequestBase


@dataclass(frozen=True)
class DeleteTitleRequest(RequestBase):
    id: int

    @staticmethod
    def from_dict(data: Dict) -> DeleteTitleRequest:
        id = data.get('id', None)
        return DeleteTitleRequest(id)


class DeleteTitle(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [IdValidator()]

    def process(self, request: DeleteTitleRequest) -> None:
        self.repository.delete(request.id)
