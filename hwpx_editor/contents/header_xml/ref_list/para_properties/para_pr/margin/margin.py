from pydantic import BaseModel, Field

from hwpx_editor.values import HWPValue


class Margin(BaseModel):
    intent: HWPValue = Field(
        default_factory=lambda: HWPValue(),
        description="""
        들여쓰기/내어쓰기
        n이 0보다 크면 들여쓰기 n
        n이 0이면 보통
        n이 0보다 작으면 내어쓰기 N
        """,
    )

    left: HWPValue = Field(
        default_factory=lambda: HWPValue(),
        description="""
        왼쪽 여백
        """,
    )

    right: HWPValue = Field(
        default_factory=lambda: HWPValue(),
        description="""
            오른쪽 여백
            """,
    )

    prev: HWPValue = Field(
        default_factory=lambda: HWPValue(),
        description="""
            위쪽 문단 간격
            """,
    )

    next: HWPValue = Field(
        default_factory=lambda: HWPValue(),
        description="""
            아래쪽 문단 간격
            """,
    )