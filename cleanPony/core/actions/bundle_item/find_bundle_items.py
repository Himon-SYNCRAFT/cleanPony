from __future__ import annotations
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validators.filter_validator import FilterValidator
from cleanPony.core.validators.pagination_validator import PaginationValidator
from cleanPony.core.requests import FindRequest


class FindBundleItems(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [FilterValidator(), PaginationValidator()]

    def process(self, request: FindRequest) -> None:
        self.repository.find(request.filters)
