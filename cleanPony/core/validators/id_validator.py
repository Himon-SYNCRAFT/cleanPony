from cleanPony.core.validator_base import ValidatorBase
from typing import Any


class IdValidator(ValidatorBase):
    def _validate(self, request: Any):
        if not hasattr(request, 'id'):
            self._add_error('Id is required')
        elif type(request.id) is not int:
            self._add_error('Id should be type of int')
