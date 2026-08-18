# FastAPI AI Agent Backend Starter Kit

레이어드 아키텍처를 기반으로 한 FastAPI 백엔드 API 스타터 킷입니다.

## 프로젝트 구조

```
fastapi_starter_kit/
├── main.py                 # 애플리케이션 진입점
├── requirements.txt        # 의존성 목록
├── .env.example           # 환경 변수 예시
├── app/
│   ├── core/
│   │   ├── config.py      # 환경 변수 및 설정
│   │   └── exceptions.py  # 커스텀 예외 정의
│   ├── api/
│   │   └── routes.py      # API 라우터 (Controller)
│   ├── services/
│   │   └── example_service.py  # 비즈니스 로직 (Service)
│   ├── repositories/
│   │   └── example_repository.py  # 데이터 접근 (Repository)
│   └── schemas/
│       └── dto.py         # 요청/응답 DTO
```

## 아키텍처

### 계층별 책임

- **Controller (API Routes)**: HTTP 요청 처리, 입력 검증
- **Service**: 비즈니스 로직, 예외 처리
- **Repository**: 데이터 접근, DB 쿼리
- **DTO**: 요청/응답 데이터 구조 정의

### 의존성 주입 (Dependency Injection)

```python
def get_example_service() -> ExampleService:
    repository = ExampleRepository(session)
    return ExampleService(repository)

@router.get("/examples/{example_id}")
async def get_example(
    example_id: int,
    service: ExampleService = Depends(get_example_service)
):
    return service.get_example(example_id)
```

## 설치 및 실행

### 1. 환경 설정

```bash
# .env 파일 생성
cp .env.example .env

# 환경 변수 수정 (.env 파일)
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3. 애플리케이션 실행

```bash
python main.py
```

또는

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 4. API 문서 접근

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API 엔드포인트

### Health Check
- `GET /api/v1/health` - 서버 상태 확인

### Examples
- `POST /api/v1/examples` - 예시 생성
- `GET /api/v1/examples` - 모든 예시 조회
- `GET /api/v1/examples/{example_id}` - 특정 예시 조회
- `PATCH /api/v1/examples/{example_id}` - 예시 수정
- `DELETE /api/v1/examples/{example_id}` - 예시 삭제

## 에러 처리

모든 예외는 일관된 응답 형식으로 반환됩니다:

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "에러 메시지",
    "details": null
  }
}
```

## 환경 변수

| 변수 | 설명 | 기본값 |
|------|------|--------|
| `ENV` | 실행 환경 | development |
| `DEBUG` | 디버그 모드 | true |
| `DATABASE_URL` | 데이터베이스 연결 문자열 | postgresql://... |
| `SECRET_KEY` | JWT 서명 키 | (필수 변경) |
| `OPENAI_API_KEY` | OpenAI API 키 | (선택) |
| `CLAUDE_API_KEY` | Claude API 키 | (선택) |

## 다음 단계

1. **데이터베이스 연결**
   - `app/repositories/example_repository.py`의 주석 처리된 부분을 활성화
   - SQLAlchemy 모델 정의

2. **LangGraph 통합**
   - `app/services/`에 Agent 서비스 추가
   - LangGraph 상태 관리 구현

3. **인증 추가**
   - JWT 토큰 인증 미들웨어
   - 사용자 권한 관리

4. **테스트 작성**
   - pytest를 사용한 유닛 테스트
   - 통합 테스트

## 라이선스

MIT
