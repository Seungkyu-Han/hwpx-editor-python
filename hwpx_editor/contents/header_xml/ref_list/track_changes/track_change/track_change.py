from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class TrackChange(BaseModel):

    type: Literal[
        "UnKnown",
        "Insert",
        "Delete",
        "CharShape",
        "ParaShape",
    ] = Field(
        description="""
        변경 추적의 종류
        UnKnown: 없음
        Insert: 삽입
        Delete: 삭제
        CharShape: 글자 서식 변경
        ParaShape: 문단 서식 변경
        """
    )

    date: datetime = Field(
        lambda: datetime.now(),
    )

    author_id: int = Field(
        ge=0,
        description="""
        변경 추적 검토자를 구별하기 위한 아이디
        """
    )

    char_shape_id: int = Field(
        ge=0,
        description="""
        변경 추적 글자의 서식 정보
        """
    )

    para_shape_id: int = Field(
        ge=0,
        description="""
        변경 추적 문단의 서식 정보
        """
    )

    hide: int = Field(
        default=0,
    )

    id: int = Field(
        ge=0,
    )