class WpApiError(Exception):
    def __init__(self, status_code, code='', message='', data={}):
        super(WpApiError, self).__init__(message)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.data = data

    @staticmethod
    def factory(response):
        status_code = response.status_code
        payload = response.json()
        code = payload['code']
        message = payload['message']
        data = payload['data']
        if status_code == 400:
            return BadRequestWpApiError(code, message, data)
        elif status_code == 401:
            return UnauthorizedWpApiError(code, message, data)
        elif status_code == 403:
            return ForbiddenWpApiError(code, message, data)
        elif status_code == 404:
            return NotFoundWpApiError(code, message, data)
        else:
            return WpApiError(status_code, code, message, data)


class BadRequestWpApiError(WpApiError):
    def __init__(self, code='', message='', data={}):
        super(BadRequestWpApiError, self).__init__(400, code, message, data)


class UnauthorizedApiErro(WpApiError):
    def __init__(self, code='', message='', data={}):
        super(NotFoundWpApiError, self).__init__(401, code, message, data)


class ForbiddenWpApiError(WpApiError):
    def __init__(self, code='', message='', data={}):
        super(ForbiddenWpApiError, self).__init__(403, code, message, data)


class NotFoundWpApiError(WpApiError):
    def __init__(self, code='', message='', data={}):
        super(NotFoundWpApiError, self).__init__(404, code, message, data)