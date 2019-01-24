from .exceptions import InvalidOperatorError
from enum import Enum, unique
from typing import Any, Set, Union


@unique
class FilterType(Enum):
    EQ: str = 'EQ'
    LT: str = 'LT'
    LE: str = 'LE'
    NE: str = 'NE'
    GE: str = 'GE'
    GT: str = 'GT'
    IN: str = 'IN'
    NOT_IN: str = 'NOT_IN'
    LIKE: str = 'LIKE'


class Filter:
    __slots__ = ['filter', 'operator', 'value', 'allowed_operators']

    def __init__(self, filter: str, value: Any, operator: Union[str, FilterType] = FilterType.EQ):

        if type(operator) is str:
            try:
                operator = FilterType(operator.capitalize())
            except ValueError as e:
                raise InvalidOperatorError from e
        elif type(operator) is FilterType:
            operator = operator
        else:
            raise InvalidOperatorError(f'{operator} is not valid value for operator')

        super(Filter, self).__setattr__('filter', filter)
        super(Filter, self).__setattr__('operator', operator)
        super(Filter, self).__setattr__('value', value)
        super(Filter, self).__setattr__('allowed_operators', set(FilterType.__members__.values()))
