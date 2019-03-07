from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
from cleanPony.core.entities import (Warranty, ReturnPolicy, ImpliedWarranty, AllegroAccount)
from typing import (List, Dict, Optional)
from datetime import datetime


class SaveAllegroAccount(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [SaveAllegroAccountValidator()]

    def process(self, request: SaveAllegroAccountRequest) -> AllegroAccount:
        allegro_account = AllegroAccount.from_dict(request.to_dict())
        return self.repository.save(allegro_account)


@dataclass
class SaveAllegroAccountRequest(RequestBase):
    id: Optional[int]
    name: Optional[str]
    hash_password: Optional[str]
    web_api_key: Optional[str]
    is_active: bool
    token: Optional[str]
    token_expiration_date: Optional[datetime]
    rest_app_id: Optional[str]
    rest_app_secret: Optional[str]
    refresh_token: Optional[str]
    rest_app_redirect: Optional[str]
    is_main: bool
    implied_warranties: List[ImpliedWarranty]
    return_policies: List[ReturnPolicy]
    warranties: List[Warranty]

    @staticmethod
    def from_dict(data: Dict) -> SaveAllegroAccountRequest:
        id = data.get("id", None)
        name = data.get("name", None)
        hash_password = data.get("hash_password", None)
        web_api_key = data.get("web_api_key", None)
        is_active = data.get("is_active", None)
        token = data.get("token", None)
        token_expiration_date = data.get("token_expiration_date", None)
        rest_app_id = data.get("rest_app_id", None)
        rest_app_secret = data.get("rest_app_secret", None)
        refresh_token = data.get("refresh_token", None)
        rest_app_redirect = data.get("rest_app_redirect", None)
        is_main = data.get("is_main", None)
        implied_warranties = data.get("implied_warranties", None)
        return_policies = data.get("return_policies", None)
        warranties = data.get("warranties", None)

        return SaveAllegroAccountRequest(
            id=id,
            name=name,
            hash_password=hash_password,
            web_api_key=web_api_key,
            is_active=is_active,
            token=token,
            token_expiration_date=token_expiration_date,
            rest_app_id=rest_app_id,
            rest_app_secret=rest_app_secret,
            refresh_token=refresh_token,
            rest_app_redirect=rest_app_redirect,
            is_main=is_main,
            implied_warranties=implied_warranties,
            return_policies=return_policies,
            warranties=warranties,
        )


class SaveAllegroAccountValidator(ValidatorBase):
    def _validate(self, request):
        pass
