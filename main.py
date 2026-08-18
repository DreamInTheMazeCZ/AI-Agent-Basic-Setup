import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.core.exceptions import AppException, create_error_response
from app.api.routes import router

# 로깅 설정
logging.basicConfig(level=settings.log_level)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 시작 이벤트
    logger.info(f"Application started: {settings.api_title}")
    yield
    # 종료 이벤트
    logger.info("Application shutdown")


# FastAPI 앱 생성
app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
    description="AI Agent Backend API Starter Kit",
    lifespan=lifespan,
)


# 예외 핸들러
@app.exception_handler(AppException)
async def app_exception_handler(request, exc: AppException):
    """애플리케이션 예외 핸들러"""
    logger.error(f"Application error: {exc.message}", exc_info=exc)
    return JSONResponse(
        status_code=exc.status_code,
        content=create_error_response(exc),
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    """요청 검증 예외 핸들러"""
    logger.warning(f"Validation error: {exc}")
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "요청 데이터가 유효하지 않습니다",
                "details": exc.errors(),
            },
        },
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc: Exception):
    """일반 예외 핸들러"""
    logger.error(f"Unexpected error: {str(exc)}", exc_info=exc)
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": {
                "code": "INTERNAL_SERVER_ERROR",
                "message": "서버 내부 오류가 발생했습니다",
            },
        },
    )


# 라우터 등록
app.include_router(router, prefix=settings.api_prefix)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        log_level=settings.log_level.lower(),
    )
