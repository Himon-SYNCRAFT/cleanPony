from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from cleanPony.core.entities import (AttributeValue, Auction, Product, DescriptionItem, Title, Image, VertoAttribute, Delivery, BundleItem, Category)
from typing import (List, Dict, Optional)
from decimal import Decimal


class SaveProduct(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveProductValidator()]

    def process(self, request: SaveProductRequest) -> Product:
        product = Product.from_dict(request.to_dict())
        return self.repository.save(product)


@dataclass
class SaveProductRequest(RequestBase):
    id: Optional[int]
    name: Optional[str]
    sku: Optional[str]
    price: Optional[Decimal]
    price_2: Optional[Decimal]
    quantity: Optional[int]
    short_description: Optional[str]
    is_bundle: bool
    is_updated: bool
    delivery: Optional[Delivery]
    attributes: List[AttributeValue]
    auctions: List[Auction]
    bundle_items: List[BundleItem]
    categories: List[Category]
    description: List[DescriptionItem]
    images: List[Image]
    titles: List[Title]
    verto_attributes: List[VertoAttribute]

    @staticmethod
    def from_dict(data: Dict) -> SaveProductRequest:
        id = data.get("id", None)
        name = data.get("name", None)
        sku = data.get("sku", None)
        price = data.get("price", None)
        price_2 = data.get("price_2", None)
        quantity = data.get("quantity", None)
        short_description = data.get("short_description", None)
        is_bundle = data.get("is_bundle", None)
        is_updated = data.get("is_updated", None)
        delivery = data.get("delivery", None)
        attributes = data.get("attributes", None)
        auctions = data.get("auctions", None)
        bundle_items = data.get("bundle_items", None)
        categories = data.get("categories", None)
        description = data.get("description", None)
        images = data.get("images", None)
        titles = data.get("titles", None)
        verto_attributes = data.get("verto_attributes", None)

        return SaveProductRequest(
            id=id,
            name=name,
            sku=sku,
            price=price,
            price_2=price_2,
            quantity=quantity,
            short_description=short_description,
            is_bundle=is_bundle,
            is_updated=is_updated,
            delivery=delivery,
            attributes=attributes,
            auctions=auctions,
            bundle_items=bundle_items,
            categories=categories,
            description=description,
            images=images,
            titles=titles,
            verto_attributes=verto_attributes,
        )


class SaveProductValidator(ValidatorBase):
    def _validate(self, request):
        pass
