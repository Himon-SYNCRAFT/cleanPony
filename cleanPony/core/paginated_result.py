from dataclasses import dataclass, field
from cleanPony.core.entities import Entity
from typing import List


@dataclass(frozen=True)
class PaginatedResult:
    items: List[Entity] = field(default_factory=list)
    page: int = 1
    page_size: int = 10
