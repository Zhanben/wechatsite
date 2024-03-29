

class BaseError(Exception):

    default_ret_code = 0

    LEVEL_DEBUG = 0
    LEVEL_INFO = 1
    LEVEL_WARN = 2
    LEVEL_ERROR = 3

    def __init__(self, message, status_code=None, extras=None, parent_error=None):
        self.message = message
        self.ret_code = status_code
        self.extras = extras
        self.parent_error = parent_error
        self.level = BaseError.LEVEL_DEBUG

    @property
    def status_code(self):
        if not self.ret_code:
            return BaseError.default_ret_code
        return self.ret_code

    def to_dict(self):
        rv = {
            'Message': self.message,
            'RetCode': self.ret_code
        }
        return rv


class ValidationError(BaseError):
    def __init__(self, message, extras=None):
        super(ValidationError, self).__init__(message=message, extras=extras)
        self.level = BaseError.LEVEL_INFO


class NotFoundError(BaseError):
    def __init__(self, message, extras=None):
        super(NotFoundError, self).__init__(message=message, extras=extras)
        self.level = BaseError.LEVEL_WARN


class FormError(BaseError):
    def __init__(self, form):
        message = form.get_validate_error()
        super(FormError, self).__init__(message, extras=form.data)
        self.level = BaseError.LEVEL_INFO


class OrmError(BaseError):
    def __init__(self, message, status_code=None, extras=None, parent_error=None):
        super(OrmError, self).__init__(message, status_code, extras, parent_error)
        self.level = BaseError.LEVEL_ERROR
