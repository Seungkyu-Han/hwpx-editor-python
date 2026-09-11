from typing import Any, Literal
from lxml.etree import QName

from lxml import etree
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

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "horizontal": str(self.horizontal),
            "vertical": str(self.vertical),
        }

        element = etree.Element(q_name, attrib=attribs)

        return element
