import traceback


class ResponseError:
    SYSTEM_ERROR = 'SYSTEM_ERROR'
    VALIDATION_ERROR = 'VALIDATION_ERROR'
    NOT_FOUND_ERROR = 'NOT_FOUND_ERROR'
    ALLEGRO_ERROR = 'ALLEGRO_ERROR'
    VERTO_ERROR = 'VERTO_ERROR'
    AUTHORIZATION_ERROR = 'AUTHORIZATION_ERROR'
    AUTHENTICATION_ERROR = 'AUTHENTICATION_ERROR'

    def __init__(self, message, error_type=SYSTEM_ERROR, stack=None):
        self.message = message
        self.type = error_type

        if stack is None:
            self.stack = traceback.format_exc()

        else:
            self.stack = stack

    def __repr__(self):
        return '{}: {}'.format(self.type, str(self.message))
