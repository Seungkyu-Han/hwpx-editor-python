from typing import Literal

from pydantic import BaseModel, Field


class Align(BaseModel):
    horizontal: Literal["JUSTIFY", "LEFT", "RIGHT", "CENTER", "DISTRIBUTE", "DISTRIBUTE_SPACE"] = Field(
        default="LEFT",
        description="""
        가로 정렬 방식
        JUSTIFY: 양쪽 정렬
        LEFT: 왼쪽 정렬
        RIGHT: 오른쪽 정렬
        CENTER: 가운데 정렬
        DISTRIBUTE: 배분 정렬
        DISTRIBUTE_SPACE: 나눔 정렬
        """
    )

    vertical: Literal["BASELINE", "TOP", "CENTER", "BOTTOM"] = Field(
        default="TOP",
        description="""
        세로 정렬 방식
        BASELINE: 글꼴 기준
        TOP: 위쪽
        CENTER: 가운데
        BOTTOM: 아래
        """
    )
