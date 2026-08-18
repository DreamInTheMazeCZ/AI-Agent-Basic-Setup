from typing import Optional, List
from app.repositories.example_repository import ExampleRepository
from app.core.exceptions import ResourceNotFoundError, ValidationError


class ExampleService:
    """예시 비즈니스 로직 계층"""

    def __init__(self, repository: ExampleRepository):
        self.repository = repository

    def create_example(self, title: str, description: Optional[str] = None) -> dict:
        """예시 생성"""
        if not title or len(title.strip()) == 0:
            raise ValidationError("title은 비어있을 수 없습니다")

        return self.repository.create(title=title, description=description)

    def get_example(self, example_id: int) -> dict:
        """ID로 예시 조회"""
        example = self.repository.get_by_id(example_id)
        if not example:
            raise ResourceNotFoundError("Example", example_id)
        return example

    def get_all_examples(self, skip: int = 0, limit: int = 10) -> List[dict]:
        """모든 예시 조회"""
        if skip < 0 or limit < 1:
            raise ValidationError("skip은 0 이상, limit은 1 이상이어야 합니다")

        return self.repository.get_all(skip=skip, limit=limit)

    def update_example(
        self, example_id: int, title: Optional[str] = None, description: Optional[str] = None
    ) -> dict:
        """예시 수정"""
        example = self.repository.get_by_id(example_id)
        if not example:
            raise ResourceNotFoundError("Example", example_id)

        if title is not None and len(title.strip()) == 0:
            raise ValidationError("title은 비어있을 수 없습니다")

        return self.repository.update(example_id=example_id, title=title, description=description)

    def delete_example(self, example_id: int) -> bool:
        """예시 삭제"""
        example = self.repository.get_by_id(example_id)
        if not example:
            raise ResourceNotFoundError("Example", example_id)

        return self.repository.delete(example_id)
