from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime


class ResponseBase(BaseModel):
    """기본 응답 DTO"""

    success: bool = True
    message: Optional[str] = None
    data: Optional[Any] = None


class ErrorResponse(BaseModel):
    """에러 응답 DTO"""

    success: bool = False
    error: dict = Field(
        ...,
        example={
            "code": "ERROR_CODE",
            "message": "Error message",
            "details": None,
        },
    )


class HealthCheckResponse(BaseModel):
    """헬스 체크 응답 DTO"""

    status: str = "healthy"
    version: str
    timestamp: datetime


class ExampleCreateRequest(BaseModel):
    """예시 생성 요청 DTO"""

    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)


class ExampleUpdateRequest(BaseModel):
    """예시 수정 요청 DTO"""

    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)


class ExampleResponse(BaseModel):
    """예시 응답 DTO"""

    id: int
    title: str
    description: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
