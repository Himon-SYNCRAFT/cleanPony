from cleanPony.core.validator_base import ValidatorBase


class IdValidator(ValidatorBase):
    def _validate(self, *args, **kwargs):
        request = kwargs.get('request', args[0])

        if not hasattr(request, 'id'):
            self._add_error('Id is required')
        elif type(request.id) is not int:
            self._add_error('Id should be type of int')
