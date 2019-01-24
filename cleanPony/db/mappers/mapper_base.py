from typing import Type

from cleanPony.db.models import Entity as Model
from cleanPony.core.repositories import Entity


class MapperBase:
    def __init__(self, model_cls: Type[Model], entity_cls: Type[Entity]) -> None:
        self._Entity = entity_cls
        self._Model = model_cls

    def to_entity(self, location: Model) -> Entity:
        return self._Entity.from_dict(location.to_dict())

    def to_model(self, location: Entity) -> Model:
        result = self._Model(**location.to_dict())
        return result
