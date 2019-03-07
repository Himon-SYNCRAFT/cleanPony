from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from typing import (Dict, Optional)
from builtins import float
from cleanPony.core.entities import Attribute


class SaveAttribute(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveAttributeValidator()]

    def process(self, request: SaveAttributeRequest) -> Attribute:
        attribute = Attribute.from_dict(request.to_dict())
        return self.repository.save(attribute)


@dataclass
class SaveAttributeRequest(RequestBase):
    id: Optional[int]
    name: Optional[str]
    type: Optional[str]
    is_required: bool
    multiple_choices: bool
    unit: Optional[str]
    values: Optional[str]
    is_range: bool
    min: Optional[float]
    max: Optional[float]
    precision: Optional[int]
    max_length: Optional[int]
    min_length: Optional[int]

    @staticmethod
    def from_dict(data: Dict) -> SaveAttributeRequest:
        id = data.get("id", None)
        name = data.get("name", None)
        type = data.get("type", None)
        is_required = data.get("is_required", None)
        multiple_choices = data.get("multiple_choices", None)
        unit = data.get("unit", None)
        values = data.get("values", None)
        is_range = data.get("is_range", None)
        min = data.get("min", None)
        max = data.get("max", None)
        precision = data.get("precision", None)
        max_length = data.get("max_length", None)
        min_length = data.get("min_length", None)

        return SaveAttributeRequest(
            id=id,
            name=name,
            type=type,
            is_required=is_required,
            multiple_choices=multiple_choices,
            unit=unit,
            values=values,
            is_range=is_range,
            min=min,
            max=max,
            precision=precision,
            max_length=max_length,
            min_length=min_length,
        )


class SaveAttributeValidator(ValidatorBase):
    def _validate(self, request):
        pass
