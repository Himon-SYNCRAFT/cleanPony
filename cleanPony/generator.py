import os
from cleanPony.core.entities import Entity, ValueObject
from stringcase import snakecase
from typing import List, Type, get_type_hints, Any, Set, Dict
from inflect import engine
from dataclasses import fields
from collections import defaultdict


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

    @staticmethod
    def _get_all_type_hints(obj: Any) -> Set:
        type_hints = list(get_type_hints(obj).values())
        result = set()

        for type_hint in type_hints:
            if type_hint in [int, str, None, bool]:
                continue

            result.add(type_hint)

            if hasattr(type_hint, '__args__'):
                for arg in type_hint.__args__:
                    if arg in [int, str, type(None), bool]:
                        continue

                    if arg.__module__ == 'typing':
                        result = result | ActionGenerator._get_all_type_hints(arg)
                    else:
                        result.add(arg)

        return result

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

    def process(self, request: {request_name}) -> PaginatedResult:
        items = self.repository.find(
            filters=request.filters,
            page=request.page,
            page_size=request.page_size
        )

        return PaginatedResult(
            items=request.filters,
            page=request.page,
            page_size=request.page_size
        )
"""

        imports = \
            f"""from __future__ import annotations
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validators.filter_validator import FilterValidator
from cleanPony.core.validators.pagination_validator import PaginationValidator
from cleanPony.core.paginated_result import PaginatedResult
from cleanPony.core.requests import {request_name}
"""
        self._write_file(file_path, [imports, action_content])

    def save(self):
        name = self.entity_name
        var_name = snakecase(name)

        file_name = f'save_{snakecase(name)}'
        dir_path = f'./cleanPony/core/actions/{snakecase(name)}'
        file_path = f'{dir_path}/{file_name}.py'

        request_name = f'Save{name}Request'
        action_name = f'Save{name}'
        validator_name = f'Save{name}Validator'

        entity_fields = fields(self._Entity)

        add_optional = any('Optional' in field.type for field in entity_fields)
        remove_union = all('Union' not in field.type for field in entity_fields)

        type_hints = self._get_all_type_hints(self._Entity)

        imports: Dict = defaultdict(set)

        for i in type_hints:
            value = None

            if hasattr(i, '__qualname__'):
                value = i.__qualname__
            elif hasattr(i, '__origin__'):
                value = i.__origin__

                if hasattr(value, '__qualname__'):
                    value = value.__qualname__.capitalize()
                else:
                    value = value._name

            if value:
                imports[i.__module__].add(value)

        if 'typing' in imports:
            if add_optional:
                imports['typing'].add('Optional')

            if remove_union:
                imports['typing'].discard('Union')

        imports['typing'].add('Dict')
        imports[self.import_path].add(name)

        imports2 = []

        for key, value in imports.items():
            classes = [str(v) for v in value]
            str_classes = ', '.join(classes)

            if len(classes) == 1:
                imports2.append(f'from {key} import {str_classes}')
            else:
                imports2.append(f'from {key} import ({str_classes})')

        imports2 = '\n'.join(imports2)

        request_fields = '\n'.join([f'    {field.name}: {field.type}' for field in entity_fields])
        request_from_dict = '\n'.join([f'        {field.name} = data.get("{field.name}", None)' for field in entity_fields])
        request_return = f'\n        return {request_name}(\n'
        request_return += '\n'.join([f'            {field.name}={field.name},' for field in entity_fields])
        request_return += '\n        )'

        action_content = \
            f"""

class {action_name}(ActionBase):
    def __init__(self, repository: CrudRepository) -> None:
        super().__init__()
        self.repository = repository
        self._validators = [{validator_name}()]

    def process(self, request: {request_name}) -> {name}:
        {var_name} = {name}.from_dict(request.to_dict())
        return self.repository.save({var_name})


@dataclass
class {request_name}(RequestBase):
{request_fields}

    @staticmethod
    def from_dict(data: Dict) -> {request_name}:
{request_from_dict}
{request_return}


class {validator_name}(ValidatorBase):
    def _validate(self, request):
        pass
"""

        imports = \
            f"""from __future__ import annotations
from dataclasses import dataclass
from cleanPony.core.actions.action_base import ActionBase
from cleanPony.core.requests import RequestBase
from cleanPony.core.repositories import CrudRepository
from cleanPony.core.validator_base import ValidatorBase
{imports2}
"""
        self._write_file(file_path, [imports, action_content])

    def generate_all(self):
        self.get()
        self.delete()
        self.find()
        self.save()


