from cleanPony.core.validator_base import ValidatorBase
from cleanPony.core.requests import PaginationRequest


class PaginationValidator(ValidatorBase):
    def _validate(self, *args, **kwargs):
        request: PaginationRequest = kwargs.get('request', args[0])

        if hasattr(request, 'page') and request.page is not int:
            self._add_error('page should be type of int')

        if hasattr(request, 'page_size') and request.page_size is not int:
            self._add_error('page_size should be type of int')
