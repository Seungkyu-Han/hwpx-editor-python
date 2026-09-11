from typing import Any, Literal
from lxml.etree import QName

from lxml import etree
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

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "type": str(self.type),
            "value": str(self.value),
            "unit": str(self.unit),
        }

        element = etree.Element(q_name, attrib=attribs)

        return element
