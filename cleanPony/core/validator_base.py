class ValidatorBase:
    def __init__(self):
        self.errors = []

    def _add_error(self, message):
        self.errors.append(message)

    def _has_errors(self):
        return len(self.errors) > 0

    def _validate(self, *args, **kwargs):
        raise NotImplementedError

    def is_valid(self, *args, **kwargs):
        self.errors = []
        self._validate(*args, **kwargs)
        return self._has_errors()
