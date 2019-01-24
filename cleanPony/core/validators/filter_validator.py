from cleanPony.core.validator_base import ValidatorBase
from cleanPony.core.requests import FindRequest


class FilterValidator(ValidatorBase):
    def _validate(self, *args, **kwargs):
        request: FindRequest = kwargs.get('request', args[0])

        if not hasattr(request, 'filters'):
            self._add_error('filters is required')
        elif type(request.filters) is not list:
            self._add_error('filters should be type of List[Filter]')

        for filter in request.filters:
            if not hasattr(filter, 'filter'):
                self._add_error("All filter's items should has filter parameter")
            elif type(filter) is not str:
                self._add_error('Filter.filter should be type of str')

            if not hasattr(filter, 'value'):
                self._add_error('Filter.value is required')
