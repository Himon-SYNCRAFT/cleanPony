from .exceptions import InvalidOperatorError
from enum import Enum, unique
from typing import Any


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
    allowed_operators = list(FilterType.__members__.values())
    __slots__ = ['filter', 'operator', 'value']

    def __init__(self, filter: str, value: Any, operator: FilterType = FilterType.EQ):
        if operator not in self.allowed_operators:
            raise InvalidOperatorError(operator)

        if operator in [FilterType.IN, FilterType.NOT_IN]:
            operator = '{}_'.format(operator)
        elif operator != FilterType.LIKE:
            operator = '__{}__'.format(operator)

        super(Filter, self).__setattr__('filter', filter)
        super(Filter, self).__setattr__('operator', operator)
        super(Filter, self).__setattr__('value', value)

    def __hash__(self):
        return hash((self.filter, self.operator, self.value))

    def __eq__(self, other):
        if other.__class__.__qualname__ is not self.__class__.__qualname__:
            return NotImplemented
        return (self.filter, self.operator, self.value) == (
            other.filter, other.operator, other.value)
