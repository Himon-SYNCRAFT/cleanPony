from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from typing import (Dict, Optional)
from cleanPony.core.entities import (Image, DescriptionItemType, DescriptionItem)


class SaveDescriptionItem(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveDescriptionItemValidator()]

    def process(self, request: SaveDescriptionItemRequest) -> DescriptionItem:
        description_item = DescriptionItem.from_dict(request.to_dict())
        return self.repository.save(description_item)


@dataclass
class SaveDescriptionItemRequest(RequestBase):
    id: Optional[int]
    header: Optional[str]
    text: Optional[str]
    image_1: Optional[Image]
    image_2: Optional[Image]
    not_for_allegro: bool
    sort: Optional[int]
    is_description_2: bool
    is_static_block: bool
    is_bundle_item: bool
    description_item_type: Optional[DescriptionItemType]

    @staticmethod
    def from_dict(data: Dict) -> SaveDescriptionItemRequest:
        id = data.get("id", None)
        header = data.get("header", None)
        text = data.get("text", None)
        image_1 = data.get("image_1", None)
        image_2 = data.get("image_2", None)
        not_for_allegro = data.get("not_for_allegro", None)
        sort = data.get("sort", None)
        is_description_2 = data.get("is_description_2", None)
        is_static_block = data.get("is_static_block", None)
        is_bundle_item = data.get("is_bundle_item", None)
        description_item_type = data.get("description_item_type", None)

        return SaveDescriptionItemRequest(
            id=id,
            header=header,
            text=text,
            image_1=image_1,
            image_2=image_2,
            not_for_allegro=not_for_allegro,
            sort=sort,
            is_description_2=is_description_2,
            is_static_block=is_static_block,
            is_bundle_item=is_bundle_item,
            description_item_type=description_item_type,
        )


class SaveDescriptionItemValidator(ValidatorBase):
    def _validate(self, request):
        pass
