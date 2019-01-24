from __future__ import annotations
from cleanPony.core.entities import Auction
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validators.id_validator import IdValidator
from cleanPony.core.requests import IdRequest


class GetAuction(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [IdValidator()]

    def process(self, request: IdRequest) -> Auction:
        return self.repository.get(request.id)
