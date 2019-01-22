from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict
from datetime import datetime, timedelta
from decimal import Decimal
from abc import ABCMeta


@dataclass(init=False)
class Entity(metaclass=ABCMeta):
    def __init__(self, *args, **kwargs):
        pass

    def to_dict(self) -> Dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(**data)


@dataclass
class AllegroAccount(Entity):
    id: Optional[int] = None
    name: Optional[str] = None
    hash_password: Optional[str] = field(default=None, repr=False)
    web_api_key: Optional[str] = None
    is_active: bool = True
    token: Optional[str] = field(default=None, repr=False)
    token_expiration_date: Optional[datetime] = None
    rest_app_id: Optional[str] = None
    rest_app_secret: Optional[str] = field(default=None, repr=False)
    refresh_token: Optional[str] = field(default=None, repr=False)
    rest_app_redirect: Optional[str] = None
    is_main: bool = False
    deliveries: List[DeliveryAllegroData] = field(default_factory=list)
    implied_warranties: List[ImpliedWarranty] = field(default_factory=list)
    return_policies: List[ReturnPolicy] = field(default_factory=list)
    warranties: List[Warranty] = field(default_factory=list)

    def update_token_expiration_date(self, seconds):
        self.token_expiration_date = datetime.now() + timedelta(seconds=seconds)


@dataclass
class Category(Entity):
    id: Optional[int] = None
    name: Optional[str] = None
    parent: Optional[Category] = None
    is_leaf: bool = False
    attributes: List[Attribute] = field(default_factory=list)

    @property
    def path(self):
        path = self.name
        if self.parent:
            path = f'{self.parent.path}/{path}'

        return path


@dataclass
class Image(Entity):
    id: Optional[int] = None
    url: Optional[str] = None
    allegro_url: Optional[str] = None
    is_main: bool = False


@dataclass
class DeliveryAllegroData(Entity):
    id: Optional[int] = None
    delivery: Optional[Delivery] = None
    account: Optional[AllegroAccount] = None


@dataclass
class ImpliedWarranty(Entity):
    id: Optional[int] = None
    name: Optional[str] = None


@dataclass
class ReturnPolicy(Entity):
    id: Optional[int] = None
    name: Optional[str] = None


@dataclass
class Warranty(Entity):
    id: Optional[int] = None
    name: Optional[str] = None


@dataclass
class Title(Entity):
    id: Optional[int] = None
    name: Optional[str] = None


@dataclass
class Product(Entity):
    id: Optional[int] = None
    name: Optional[str] = None
    sku: Optional[str] = None
    price: Optional[Decimal] = None
    price_2: Optional[Decimal] = None
    quantity: Optional[int] = None
    short_description: Optional[str] = None
    is_bundle: bool = False
    is_updated: bool = False
    delivery: Optional[Delivery] = None
    attributes: Optional[List[AttributeValue]] = field(default_factory=list)
    auctions: Optional[List[Auction]] = field(default_factory=list)
    bundle_items: Optional[List[BundleItem]] = field(default_factory=list)
    categories: Optional[List[Category]] = field(default_factory=list)
    description: Optional[List[DescriptionItem]] = field(default_factory=list)
    images: Optional[List[Image]] = field(default_factory=list)
    titles: List[Title] = field(default_factory=list)
    verto_attributes: Optional[List[VertoAttribute]] = field(default_factory=list)

    @property
    def sku_2(self):
        return self.sku + 'A'

    @property
    def main_image(self):
        images = [image for image in self.images if image.is_main]

        if images:
            return images[0]
        elif self.images[0]:
            return self.images[0]
        else:
            return None


@dataclass
class Attribute(Entity):
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None
    is_required: bool = False
    multiple_choices: bool = False
    unit: Optional[str] = None
    values: Optional[str] = None
    is_range: bool = False
    min: Optional[float] = None
    max: Optional[float] = None
    precision: Optional[int] = None
    max_length: Optional[int] = None
    min_length: Optional[int] = None

    def set_values(self, values):
        values_string = []

        for item in values:
            value_id = item['id']
            value = item['value']
            val_str = '{}:{}'.format(value_id, value)

            values_string.append(val_str)

        self.values = '|'.join(values_string)


@dataclass
class AttributeValue(Entity):
    id: Optional[int] = None
    value: Optional[str] = None
    attribute: Optional[Attribute] = None


@dataclass
class DeliveryOptionType(Entity):
    id: Optional[int] = None
    name: Optional[str] = None
    is_active: bool = True


@dataclass
class DeliveryOption(Entity):
    id: Optional[int] = None
    delivery_option_type: Optional[DeliveryOptionType] = None
    delivery: Optional[Delivery] = None
    first_piece_cost: float = -1.00
    next_pieces_cost: float = -1.00
    quantity: int = -1


@dataclass
class Delivery(Entity):
    id: Optional[int] = None
    name: Optional[str] = None
    is_updated: bool = None
    delivery_options: List[DeliveryOption] = field(default_factory=list)
    allegro_data: List[DeliveryAllegroData] = field(default_factory=list)


@dataclass
class StaticBlock(Entity):
    id: Optional[int] = None
    description_item_type: Optional[DescriptionItemType] = None
    header: Optional[str] = None
    text: Optional[str] = None
    image_1: Optional[Image] = None
    image_2: Optional[Image] = None


@dataclass
class DescriptionItemType(Entity):
    id: Optional[int] = None
    name: Optional[str] = None


@dataclass
class DescriptionItem(Entity):
    id: Optional[int] = None
    header: Optional[str] = None
    text: Optional[str] = None
    image_1: Optional[Image] = None
    image_2: Optional[Image] = None
    not_for_allegro: bool = False
    sort: Optional[int] = None
    is_description_2: bool = False
    description_item_type: Optional[DescriptionItemType] = None
    static_block: Optional[StaticBlock] = None
    bundle_item: Optional[BundleItem] = None


@dataclass
class BundleItem(Entity):
    owner: Optional[Product] = None
    item: Optional[Product] = None
    quantity: int = 1


@dataclass
class AuctionType(Entity):
    id: Optional[int] = None
    name: Optional[str] = None


@dataclass
class Duration(Entity):
    id: Optional[int] = None
    name: Optional[str] = None


@dataclass
class Location(Entity):
    id: Optional[int] = None
    name: Optional[str] = None


@dataclass
class Auction(Entity):
    id: Optional[int] = None
    account: Optional[AllegroAccount] = None
    auction_number: Optional[int] = None
    auction_type: Optional[AuctionType] = None
    category: Optional[category] = None
    date: Optional[datetime] = datetime.today()
    duration: Optional[Duration] = None
    is_active: bool = False
    is_bold: bool = False
    is_emphasize: bool = False
    is_highlight: bool = False
    last_error: Optional[str] = None
    location: Optional[Location] = None
    product: Optional[Product] = None
    title: Optional[Title] = None

    @property
    def delivery(self):
        product = self.product
        account = self.account

        if product is None or account is None or product.delivery is None:
            return None

        for delivery in account.deliveries:
            if delivery.id == product.delivery.id:
                return delivery

        return None


@dataclass
class VertoAttribute(Entity):
    product: Optional[Product] = None
    definition_id: Optional[int] = None
    name: Optional[str] = None
    value: Optional[str] = None
