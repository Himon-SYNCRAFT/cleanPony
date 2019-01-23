from cleanPony.core.exceptions import NotFoundError, AllegroError, VertoError
from cleanPony.core.response_error import ResponseError
from cleanPony.core.response_base import ResponseBase
from cleanPony.core.validator_base import ValidatorBase
from typing import List


class ActionBase:
    def __init__(self, *args, **kwargs) -> None:
        self._validators: List[ValidatorBase] = []

    def execute(self, request=None) -> ResponseBase:
        response = ResponseBase()

        try:
            if request is not None:
                self._validate_request(request, response)

            if response.has_errors():
                return response

            response.data = self.process(request)

        except NotFoundError as err:
            response.add_error(ResponseError(str(err), ResponseError.NOT_FOUND_ERROR))

        except AllegroError as err:
            response.add_error(ResponseError(str(err), ResponseError.ALLEGRO_ERROR))

        except VertoError as err:
            response.add_error(ResponseError(str(err), ResponseError.VERTO_ERROR))

        except Exception as err:
            response.add_error(ResponseError(str(err)))
            raise

        return response

    def _validate_request(self, request, response: ResponseBase) -> None:
        if not self._validators:
            return

        for validator in self._validators:
            if not validator.is_valid(request):
                for error in validator.errors:
                    response.add_error(ResponseError(error, ResponseError.VALIDATION_ERROR))

    def process(self, request):
        raise NotImplementedError
