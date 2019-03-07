from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from cleanPony.core.entities import (Location, AuctionType, Duration, Product, AllegroAccount, Auction, Title, Category)
from typing import (Dict, Optional)
from datetime import datetime


class SaveAuction(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveAuctionValidator()]

    def process(self, request: SaveAuctionRequest) -> Auction:
        auction = Auction.from_dict(request.to_dict())
        return self.repository.save(auction)


@dataclass
class SaveAuctionRequest(RequestBase):
    id: Optional[int]
    account: Optional[AllegroAccount]
    auction_number: Optional[int]
    auction_type: Optional[AuctionType]
    category: Optional[Category]
    date: Optional[datetime]
    duration: Optional[Duration]
    is_active: bool
    is_bold: bool
    is_emphasize: bool
    is_highlight: bool
    last_error: Optional[str]
    location: Optional[Location]
    product: Optional[Product]
    title: Optional[Title]

    @staticmethod
    def from_dict(data: Dict) -> SaveAuctionRequest:
        id = data.get("id", None)
        account = data.get("account", None)
        auction_number = data.get("auction_number", None)
        auction_type = data.get("auction_type", None)
        category = data.get("category", None)
        date = data.get("date", None)
        duration = data.get("duration", None)
        is_active = data.get("is_active", None)
        is_bold = data.get("is_bold", None)
        is_emphasize = data.get("is_emphasize", None)
        is_highlight = data.get("is_highlight", None)
        last_error = data.get("last_error", None)
        location = data.get("location", None)
        product = data.get("product", None)
        title = data.get("title", None)

        return SaveAuctionRequest(
            id=id,
            account=account,
            auction_number=auction_number,
            auction_type=auction_type,
            category=category,
            date=date,
            duration=duration,
            is_active=is_active,
            is_bold=is_bold,
            is_emphasize=is_emphasize,
            is_highlight=is_highlight,
            last_error=last_error,
            location=location,
            product=product,
            title=title,
        )


class SaveAuctionValidator(ValidatorBase):
    def _validate(self, request):
        pass
