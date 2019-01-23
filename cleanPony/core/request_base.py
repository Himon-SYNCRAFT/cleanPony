from __future__ import annotations
from typing import Dict


class RequestBase:
    @staticmethod
    def from_dict(data: Dict) -> RequestBase:
        raise NotImplementedError
