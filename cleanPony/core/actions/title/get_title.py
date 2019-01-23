from __future__ import annotations
from dataclasses import dataclass
from typing import Dict

from cleanPony.core.entities import Title
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validators.id_validator import IdValidator
from cleanPony.core.request_base import RequestBase


@dataclass(frozen=True)
class GetTitleRequest(RequestBase):
    id: int

    @staticmethod
    def from_dict(data: Dict) -> GetTitleRequest:
        id = data.get('id', None)
        return GetTitleRequest(id)


class GetTitle(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [IdValidator()]

    def process(self, request: GetTitleRequest) -> Title:
        return self.repository.get(request.id)
