from typing import Optional

from pydantic import BaseModel, Field


class TrackChangeAuthor(BaseModel):
    name: str = Field(
        description="검토자 이름"
    )

    mark: int = Field(
        description="검토 표시 여부"
    )

    color: Optional[str] = Field(
        description="검토 표시 색상"
    )

    id: int = Field(
        description="검토자를 구별하기 위한 아이디"
    )
