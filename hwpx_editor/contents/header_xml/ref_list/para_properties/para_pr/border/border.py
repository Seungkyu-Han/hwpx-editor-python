from pydantic import BaseModel, Field


class Border(BaseModel):
    border_fill_id_ref: int = Field(
        default=0,
        description="""
        테두리/배경 모양 아이디 참조값
        """
    )
    offset_left: int = Field(
        default=0,
        description="""
        문단 테두리 왼쪽 간격. 단위는 HWPUNIT
        """
    )
    offset_right: int = Field(
        default=0,
        description="""
        문단 테두리 오른쪽 간격. 단위는 HWPUNIT
        """
    )
    offset_top: int = Field(
        default=0,
        description="""
        문단 테두리 위쪽 간격. 단위는 HWPUNIT
        """
    )
    offset_bottom: int = Field(
        default=0,
        description="""
        문단 테두리 아래쪽 간격. 단위는 HWPUNIT
        """
    )
    connect: int = Field(
        default=0,
        description="""
        문단 테두리 연결 여부
        """
    )
    ignore_margin: int = Field(
        default=0,
        description="""
        문단 테두리 여백 무시 여부
        """
    )
