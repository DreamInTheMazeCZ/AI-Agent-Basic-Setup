from fastapi import HTTPException, status
from typing import Any, Optional


class AppException(Exception):
    """기본 애플리케이션 예외"""

    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        error_code: Optional[str] = None,
        details: Optional[Any] = None,
    ):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code or "INTERNAL_SERVER_ERROR"
        self.details = details
        super().__init__(self.message)


class ValidationError(AppException):
    """유효성 검사 예외"""

    def __init__(self, message: str, details: Optional[Any] = None):
        super().__init__(
            message=message,
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            error_code="VALIDATION_ERROR",
            details=details,
        )


class ResourceNotFoundError(AppException):
    """리소스 미발견 예외"""

    def __init__(self, resource: str, resource_id: Any):
        message = f"{resource} with id {resource_id} not found"
        super().__init__(
            message=message,
            status_code=status.HTTP_404_NOT_FOUND,
            error_code="RESOURCE_NOT_FOUND",
        )


class UnauthorizedError(AppException):
    """인증 예외"""

    def __init__(self, message: str = "Unauthorized"):
        super().__init__(
            message=message,
            status_code=status.HTTP_401_UNAUTHORIZED,
            error_code="UNAUTHORIZED",
        )


class ForbiddenError(AppException):
    """권한 예외"""

    def __init__(self, message: str = "Forbidden"):
        super().__init__(
            message=message,
            status_code=status.HTTP_403_FORBIDDEN,
            error_code="FORBIDDEN",
        )


class ConflictError(AppException):
    """충돌 예외"""

    def __init__(self, message: str, details: Optional[Any] = None):
        super().__init__(
            message=message,
            status_code=status.HTTP_409_CONFLICT,
            error_code="CONFLICT",
            details=details,
        )


def create_error_response(exception: AppException) -> dict:
    """예외를 API 응답 형식으로 변환"""
    return {
        "success": False,
        "error": {
            "code": exception.error_code,
            "message": exception.message,
            "details": exception.details,
        },
    }
