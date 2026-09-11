from typing import Any
from lxml.etree import QName

from lxml import etree
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

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "borderFillIDRef": str(self.border_fill_id_ref),
            "offsetLeft": str(self.offset_left),
            "offsetRight": str(self.offset_right),
            "offsetTop": str(self.offset_top),
            "offsetBottom": str(self.offset_bottom),
            "connect": str(self.connect),
            "ignoreMargin": str(self.ignore_margin),
        }

        element = etree.Element(q_name, attrib=attribs)

        return element
