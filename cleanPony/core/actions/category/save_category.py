from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from cleanPony.core.entities import (Category, Attribute)
from typing import (List, Dict, Optional)


class SaveCategory(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveCategoryValidator()]

    def process(self, request: SaveCategoryRequest) -> Category:
        category = Category.from_dict(request.to_dict())
        return self.repository.save(category)


@dataclass
class SaveCategoryRequest(RequestBase):
    id: Optional[int]
    name: Optional[str]
    parent: Optional[Category]
    is_leaf: bool
    attributes: List[Attribute]

    @staticmethod
    def from_dict(data: Dict) -> SaveCategoryRequest:
        id = data.get("id", None)
        name = data.get("name", None)
        parent = data.get("parent", None)
        is_leaf = data.get("is_leaf", None)
        attributes = data.get("attributes", None)

        return SaveCategoryRequest(
            id=id,
            name=name,
            parent=parent,
            is_leaf=is_leaf,
            attributes=attributes,
        )


class SaveCategoryValidator(ValidatorBase):
    def _validate(self, request):
        pass
