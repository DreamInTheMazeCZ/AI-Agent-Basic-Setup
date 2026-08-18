from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete


class ExampleRepository:
    """예시 데이터 접근 계층"""

    def __init__(self, session: Session):
        self.session = session

    def create(self, title: str, description: Optional[str] = None) -> dict:
        """예시 데이터 생성"""
        # 실제 구현에서는 여기서 DB 모델을 사용
        # example = Example(title=title, description=description)
        # self.session.add(example)
        # self.session.commit()
        # return example

        # 예시용 딕셔너리 반환
        return {"id": 1, "title": title, "description": description}

    def get_by_id(self, example_id: int) -> Optional[dict]:
        """ID로 예시 데이터 조회"""
        # 실제 구현:
        # example = self.session.execute(
        #     select(Example).where(Example.id == example_id)
        # ).scalar_one_or_none()
        # return example

        return {"id": example_id, "title": "Example Title"}

    def get_all(self, skip: int = 0, limit: int = 10) -> List[dict]:
        """모든 예시 데이터 조회"""
        # 실제 구현:
        # examples = self.session.execute(
        #     select(Example).offset(skip).limit(limit)
        # ).scalars().all()
        # return examples

        return [{"id": 1, "title": "Example 1"}]

    def update(
        self, example_id: int, title: Optional[str] = None, description: Optional[str] = None
    ) -> Optional[dict]:
        """예시 데이터 수정"""
        # 실제 구현:
        # self.session.execute(
        #     update(Example)
        #     .where(Example.id == example_id)
        #     .values(title=title, description=description)
        # )
        # self.session.commit()

        return {"id": example_id, "title": title, "description": description}

    def delete(self, example_id: int) -> bool:
        """예시 데이터 삭제"""
        # 실제 구현:
        # self.session.execute(delete(Example).where(Example.id == example_id))
        # self.session.commit()

        return True
