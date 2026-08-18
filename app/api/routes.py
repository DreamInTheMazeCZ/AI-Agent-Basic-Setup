from fastapi import APIRouter, Depends, status
from datetime import datetime
from app.core.config import settings
from app.core.exceptions import AppException, create_error_response
from app.schemas.dto import (
    HealthCheckResponse,
    ExampleCreateRequest,
    ExampleUpdateRequest,
    ExampleResponse,
    ResponseBase,
)
from app.services.example_service import ExampleService
from app.repositories.example_repository import ExampleRepository


router = APIRouter()


def get_example_service() -> ExampleService:
    """서비스 의존성 주입"""
    # 실제 구현에서는 DB 세션을 주입
    # session = SessionLocal()
    # repository = ExampleRepository(session)
    repository = ExampleRepository(session=None)
    return ExampleService(repository)


@router.get(
    "/health",
    response_model=HealthCheckResponse,
    status_code=status.HTTP_200_OK,
    tags=["Health"],
)
async def health_check() -> HealthCheckResponse:
    """헬스 체크"""
    return HealthCheckResponse(
        status="healthy", version=settings.api_version, timestamp=datetime.utcnow()
    )


@router.post(
    "/examples",
    response_model=ResponseBase,
    status_code=status.HTTP_201_CREATED,
    tags=["Examples"],
)
async def create_example(
    request: ExampleCreateRequest, service: ExampleService = Depends(get_example_service)
) -> ResponseBase:
    """예시 생성"""
    try:
        example = service.create_example(title=request.title, description=request.description)
        return ResponseBase(success=True, message="예시가 생성되었습니다", data=example)
    except AppException as e:
        raise


@router.get(
    "/examples/{example_id}",
    response_model=ResponseBase,
    status_code=status.HTTP_200_OK,
    tags=["Examples"],
)
async def get_example(
    example_id: int, service: ExampleService = Depends(get_example_service)
) -> ResponseBase:
    """예시 조회"""
    try:
        example = service.get_example(example_id)
        return ResponseBase(success=True, data=example)
    except AppException as e:
        raise


@router.get(
    "/examples",
    response_model=ResponseBase,
    status_code=status.HTTP_200_OK,
    tags=["Examples"],
)
async def get_all_examples(
    skip: int = 0,
    limit: int = 10,
    service: ExampleService = Depends(get_example_service),
) -> ResponseBase:
    """모든 예시 조회"""
    try:
        examples = service.get_all_examples(skip=skip, limit=limit)
        return ResponseBase(
            success=True,
            data={"items": examples, "skip": skip, "limit": limit, "total": len(examples)},
        )
    except AppException as e:
        raise


@router.patch(
    "/examples/{example_id}",
    response_model=ResponseBase,
    status_code=status.HTTP_200_OK,
    tags=["Examples"],
)
async def update_example(
    example_id: int,
    request: ExampleUpdateRequest,
    service: ExampleService = Depends(get_example_service),
) -> ResponseBase:
    """예시 수정"""
    try:
        example = service.update_example(
            example_id=example_id, title=request.title, description=request.description
        )
        return ResponseBase(success=True, message="예시가 수정되었습니다", data=example)
    except AppException as e:
        raise


@router.delete(
    "/examples/{example_id}",
    response_model=ResponseBase,
    status_code=status.HTTP_200_OK,
    tags=["Examples"],
)
async def delete_example(
    example_id: int, service: ExampleService = Depends(get_example_service)
) -> ResponseBase:
    """예시 삭제"""
    try:
        service.delete_example(example_id)
        return ResponseBase(success=True, message="예시가 삭제되었습니다")
    except AppException as e:
        raise
