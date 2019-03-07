from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from typing import (Dict, Optional)
from cleanPony.core.entities import Image


class SaveImage(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveImageValidator()]

    def process(self, request: SaveImageRequest) -> Image:
        image = Image.from_dict(request.to_dict())
        return self.repository.save(image)


@dataclass
class SaveImageRequest(RequestBase):
    id: Optional[int]
    url: Optional[str]
    allegro_url: Optional[str]
    is_main: bool

    @staticmethod
    def from_dict(data: Dict) -> SaveImageRequest:
        id = data.get("id", None)
        url = data.get("url", None)
        allegro_url = data.get("allegro_url", None)
        is_main = data.get("is_main", None)

        return SaveImageRequest(
            id=id,
            url=url,
            allegro_url=allegro_url,
            is_main=is_main,
        )


class SaveImageValidator(ValidatorBase):
    def _validate(self, request):
        pass
