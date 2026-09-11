from typing import Any, Literal
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.values import HexColor


class Shadow(BaseModel, validate_assignment=True):
    type: Literal["NONE", "DROP", "CONTINUOUS"] = Field(default="NONE")
    color: HexColor = Field(default="#C0C0C0")
    offset_x: int = Field(default=10)
    offset_y: int = Field(default=10)

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "type": str(self.type),
            "color": str(self.color),
            "offsetX": str(self.offset_x),
            "offsetY": str(self.offset_y),
        }

        element = etree.Element(q_name, attrib=attribs)

        return element
