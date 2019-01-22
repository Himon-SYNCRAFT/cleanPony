from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.validators.id_validator import IdValidator
from cleanPony.core.repositories import CrudRepository


@dataclass(frozen=True)
class GetEntityRequest:
    id: int


class GetEntity(ActionBase):
    def __init__(self, repository: CrudRepository):
        super().__init__()
        self._validators = [IdValidator()]
        self.repository = repository

    def process(self, request):
        return self.repository.get(request.id)
