from .exceptions import InvalidOperatorError
from enum import Enum, unique
from typing import Any, Set
from dataclasses import dataclass


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


@dataclass(frozen=True)
class Filter:
    value: Any
    filter: str
    operator: FilterType = FilterType.EQ

    def __post_init__(self):
        allowed_operators: Set[FilterType] = set(FilterType.__members__.values())

        if self.operator not in allowed_operators:
            raise InvalidOperatorError(self.operator)
