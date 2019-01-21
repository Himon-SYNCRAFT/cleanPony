class NotFoundError(Exception):
    pass


class InvalidOperatorError(Exception):
    def __init__(self, operator, errors=None):
        super().__init__('Operator {} is not supported'.format(operator))

        if errors is None:
            self.errors = errors
        else:
            self.errors = errors


class ActiveAuctionRemoveError(Exception):
    pass


class AllegroError(Exception):
    pass


class VertoError(Exception):
    pass


class InvalidActionError(TypeError):
    pass


class AuthorizationError(Exception):
    pass


class RepositoryException(Exception):
    pass
