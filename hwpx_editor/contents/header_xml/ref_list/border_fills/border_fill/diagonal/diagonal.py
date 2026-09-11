from typing import Any
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.enums import LineType2

from hwpx_editor.values import HexColor


class Diagonal(BaseModel, validate_assignment=True):
    type: LineType2 = Field(default=LineType2.NONE)
    width: float = Field(default=0.12)
    color: HexColor = Field(default="#000000")

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "type": str(self.type),
            "width": f"{self.width:g} mm",
            "color": str(self.color),
        }

        element = etree.Element(q_name, attrib=attribs)

        return element
