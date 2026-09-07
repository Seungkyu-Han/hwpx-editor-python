from typing import Literal

from pydantic import BaseModel, Field


class LineSpacing(BaseModel):
    type: Literal["PERCENT"] = Field(
        default="PERCENT",
        description="""
        줄 간격 종류        
        """,
    )

    value: int = Field(
        default=160,
        description="""
        줄 간격 값
        type이 PERCENT이면 0% ~ 500%로 제한
        """
    )

    unit: Literal["HWPUNIT"] = Field(
        default="HWPUNIT",
        description="""
        줄 간격 값의 단위
        """
    )
