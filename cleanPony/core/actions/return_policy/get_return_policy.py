from __future__ import annotations
from cleanPony.core.entities import ReturnPolicy
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validators.id_validator import IdValidator
from cleanPony.core.requests import IdRequest


class GetReturnPolicy(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [IdValidator()]

    def process(self, request: IdRequest) -> ReturnPolicy:
        return self.repository.get(request.id)
