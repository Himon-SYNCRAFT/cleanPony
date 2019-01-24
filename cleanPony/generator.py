import os
from cleanPony.core.entities import Entity
from stringcase import snakecase
from typing import List, Type
from inflect import engine


inflector = engine()


class ActionGenerator:
    def __init__(self, entity_cls: Type[Entity], force_rewrite: bool = False):
        self._Entity = entity_cls
        self._force_rewrite = force_rewrite

    @property
    def entity_name(self) -> str:
        return self._Entity.__qualname__

    @property
    def import_path(self) -> str:
        return self._Entity.__module__

    def _pluralize(self, word: str):
        return inflector.plural(word)

    def _write_file(self, file_path: str, content: List[str]):
        if not self._force_rewrite and os.path.exists(file_path):
            raise FileExistsError

        dir_path = os.path.dirname(file_path)

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        with open(file_path, 'w') as file:
            for item in content:
                file.writelines(item)
            file.writelines('')

    def get(self):
        file_name = f'get_{snakecase(self.entity_name)}'
        dir_path = f'./cleanPony/core/actions/{snakecase(self.entity_name)}'
        file_path = f'{dir_path}/{file_name}.py'

        request_name = 'IdRequest'
        action_name = f'Get{self.entity_name}'

        action_content =\
            f"""

class {action_name}(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [IdValidator()]

    def process(self, request: {request_name}) -> {self.entity_name}:
        return self.repository.get(request.id)
"""

        imports =\
            f"""from __future__ import annotations
from {self.import_path} import {self.entity_name}
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validators.id_validator import IdValidator
from cleanPony.core.requests import {request_name}
"""
        self._write_file(file_path, [imports, action_content])

    def delete(self):
        file_name = f'delete_{snakecase(self.entity_name)}'
        dir_path = f'./cleanPony/core/actions/{snakecase(self.entity_name)}'
        file_path = f'{dir_path}/{file_name}.py'

        request_name = 'IdRequest'
        action_name = f'Delete{self.entity_name}'

        action_content = \
            f"""

class {action_name}(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [IdValidator()]

    def process(self, request: {request_name}) -> None:
        self.repository.delete(request.id)
"""

        imports = \
            f"""from __future__ import annotations
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validators.id_validator import IdValidator
from cleanPony.core.requests import {request_name}
"""
        self._write_file(file_path, [imports, action_content])

    def find(self):
        name = self.entity_name
        name_plural = self._pluralize(name)

        file_name = f'find_{snakecase(name_plural)}'
        dir_path = f'./cleanPony/core/actions/{snakecase(name)}'
        file_path = f'{dir_path}/{file_name}.py'

        request_name = 'FindRequest'
        action_name = f'Find{name_plural}'

        action_content = \
            f"""

class {action_name}(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [FilterValidator(), PaginationValidator()]

    def process(self, request: {request_name}) -> None:
        self.repository.find(request.filters)
"""

        imports = \
            f"""from __future__ import annotations
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validators.filter_validator import FilterValidator
from cleanPony.core.validators.pagination_validator import PaginationValidator
from cleanPony.core.requests import {request_name}
"""
        self._write_file(file_path, [imports, action_content])

    def generate_all(self):
        self.get()
        self.delete()
        self.find()


