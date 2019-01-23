from flask import jsonify
import functools
from cleanPony.core.response_base import ResponseBase
from cleanPony.core.response_error import ResponseError


def response_error(response):
    errors = [{
        'message': str(error.message),
        'type': error.type,
        'stack': error.stack or '',
    } for error in response.errors]

    status_code = 400

    if any(error.type == ResponseError.AUTHENTICATION_ERROR for error in response.errors):
        status_code = 401
    elif any(str(error.message).startswith('404') for error in response.errors):
        status_code = 404

    return jsonify({'errors': errors}), status_code


def response_to_json(response):
    if type(response) is str:
        return response

    if type(response) != ResponseBase:
        return jsonify(response)

    if response.has_errors():
        return response_error(response)

    return jsonify(response.data)


def json(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        rv = f(*args, **kwargs)

        if rv is not None:
            return response_to_json(rv)

    return wrapped


# def auth(f):
#     @functools.wraps(f)
#     def wrapped(*args, **kwargs):
#         token = request.args.get('token')
#
#         if not token:
#             error = ResponseError(
#                 message='Authorization error. You need to be logged in',
#                 error_type=ResponseError.AUTHORIZATION_ERROR,
#                 stack=''
#             )
#             return ResponseBase(errors=[error])
#
#         action = Context.get_action(IsLogged)
#         response = action.execute(IsLoggedRequest(token))
#
#         if not response.data['is_logged']:
#             error = ResponseError(
#                 message='Authorization error. You need to be logged in',
#                 error_type=ResponseError.AUTHORIZATION_ERROR,
#                 stack=''
#             )
#             return ResponseBase(errors=[error])
#
#         return f(*args, **kwargs)
#
#     return wrapped
