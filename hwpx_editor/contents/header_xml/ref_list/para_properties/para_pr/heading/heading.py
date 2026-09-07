from typing import Literal

from pydantic import BaseModel, Field


class Heading(BaseModel):
    type: Literal["NONE", "OUTLINE", "NUMBER", "BULLET"] = Field(
        default="NONE",
        description="""
        문단 머리 모양 종류
        NONE: 없음
        OUTLINE: 개요
        NUMBER: 번호
        """
    )

    id_ref: int = Field(
        default=0,
        ge=0,
        description="""
        문단 머리 번호/글머리표 모양 아이디 참조값
        """
    )

    level: int = Field(
        default=0,
        ge=0,
        description="""
        참조 단계
        """
    )