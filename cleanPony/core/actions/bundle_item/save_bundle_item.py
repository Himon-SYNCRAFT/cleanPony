from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from typing import (Dict, Optional)
from cleanPony.core.entities import (Product, BundleItem)


class SaveBundleItem(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveBundleItemValidator()]

    def process(self, request: SaveBundleItemRequest) -> BundleItem:
        bundle_item = BundleItem.from_dict(request.to_dict())
        return self.repository.save(bundle_item)


@dataclass
class SaveBundleItemRequest(RequestBase):
    owner: Optional[Product]
    item: Optional[Product]
    quantity: int

    @staticmethod
    def from_dict(data: Dict) -> SaveBundleItemRequest:
        owner = data.get("owner", None)
        item = data.get("item", None)
        quantity = data.get("quantity", None)

        return SaveBundleItemRequest(
            owner=owner,
            item=item,
            quantity=quantity,
        )


class SaveBundleItemValidator(ValidatorBase):
    def _validate(self, request):
        pass
