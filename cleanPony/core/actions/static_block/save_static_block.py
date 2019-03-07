from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from typing import (Dict, Optional)
from cleanPony.core.entities import (Image, DescriptionItemType, StaticBlock)


class SaveStaticBlock(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveStaticBlockValidator()]

    def process(self, request: SaveStaticBlockRequest) -> StaticBlock:
        static_block = StaticBlock.from_dict(request.to_dict())
        return self.repository.save(static_block)


@dataclass
class SaveStaticBlockRequest(RequestBase):
    id: Optional[int]
    description_item_type: Optional[DescriptionItemType]
    header: Optional[str]
    text: Optional[str]
    image_1: Optional[Image]
    image_2: Optional[Image]

    @staticmethod
    def from_dict(data: Dict) -> SaveStaticBlockRequest:
        id = data.get("id", None)
        description_item_type = data.get("description_item_type", None)
        header = data.get("header", None)
        text = data.get("text", None)
        image_1 = data.get("image_1", None)
        image_2 = data.get("image_2", None)

        return SaveStaticBlockRequest(
            id=id,
            description_item_type=description_item_type,
            header=header,
            text=text,
            image_1=image_1,
            image_2=image_2,
        )


class SaveStaticBlockValidator(ValidatorBase):
    def _validate(self, request):
        pass
