from cleanPony.core.paginated_result import PaginatedResult
from cleanPony.core.entities import Entity
from typing import Union, List, Dict, Optional


class ResponseBase:
    def __init__(self,
                 data: Union[List, Dict, PaginatedResult, Entity] = None,
                 errors: Optional[List] = None):
        self._data = None
        self.data = data

        if errors is None:
            self.errors = []
        else:
            self.errors = errors

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        if data is None:
            self._data = None

        elif type(data) is list:
            self._data = [item.to_dict() for item in data]

        elif type(data) is dict:
            self._data = data

        elif type(data) is PaginatedResult:
            self._data = dict(
                page=data.page,
                page_size=data.page_size,
                items=[]
            )

            for item in data.items:
                self._data['items'].append(item.to_dict())

        else:
            self._data = data.to_dict()

    def has_errors(self):
        return len(self.errors) > 0

    def add_error(self, error):
        self.errors.append(error)

    def __repr__(self):
        return f'{self.__class__.__name__}(data={repr(self.data)}, errors={repr(self.errors)})'
