from logging import getLogger
from typing import ClassVar

from fastapi import status
from fastapi.responses import JSONResponse

from {{ cookiecutter.project_slug }}.business.exceptions import BusinessConflict, ObjectNotFound

logger = getLogger(__name__)

class CustomPresentationException(Exception):
    STATUS_CODE: ClassVar[int] = status.HTTP_500_INTERNAL_SERVER_ERROR
    MESSAGE: ClassVar[str] = 'Internal Server Error'

    def __init__(self, message: str | None = None):
        self.status_code = self.STATUS_CODE
        self.message = message or self.MESSAGE
        super().__init__(f'{self.status_code} - {self.message}')


class BadRequestException(CustomPresentationException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    MESSAGE = 'Bad Request'


class ConflictException(CustomPresentationException):
    STATUS_CODE = status.HTTP_409_CONFLICT
    MESSAGE = 'Conflict'


class NotAuthorizedException(CustomPresentationException):
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    MESSAGE = 'Unauthorized'


class ForbiddenException(CustomPresentationException):
    STATUS_CODE = status.HTTP_403_FORBIDDEN
    MESSAGE = 'Forbidden'


class NotFoundException(CustomPresentationException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    MESSAGE = 'Not Found'


class BadGatewayException(CustomPresentationException):
    STATUS_CODE = status.HTTP_502_BAD_GATEWAY
    MESSAGE = 'Bad Gateway'


class ValidationException(CustomPresentationException):
    STATUS_CODE = status.HTTP_422_UNPROCESSABLE_ENTITY
    MESSAGE = 'Validation Error'


class HttpResponseException:
    def __init__(self, exc: Exception):
        logger.error(repr(exc))

        if isinstance(exc, BusinessConflict):
            exc = ConflictException()

        if isinstance(exc, ObjectNotFound):
            exc = NotFoundException()

        self.status_code = getattr(exc, 'STATUS_CODE', 500)
        self.content = getattr(exc, 'MESSAGE', 'Internal Server Error')

    def get_response(self):
        return JSONResponse(
            status_code=self.status_code,
            content={'error_message': self.content},
        )
