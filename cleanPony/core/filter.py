from .exceptions import InvalidOperatorError


class Filter:
    allowed_operators = ['eq', 'lt', 'le', 'ne', 'ge', 'gt', 'in', 'notin', 'like']
    __slots__ = ['filter', 'operator', 'value']

    def __init__(self, filter: str, value: str, operator: str = 'eq'):

        if operator not in self.allowed_operators:
            raise InvalidOperatorError(operator)

        if operator in ['in', 'notin']:
            operator = '{}_'.format(operator)
        elif operator != 'like':
            operator = '__{}__'.format(operator)

        super(Filter, self).__setattr__('filter', filter)
        super(Filter, self).__setattr__('operator', operator)
        super(Filter, self).__setattr__('value', value)
