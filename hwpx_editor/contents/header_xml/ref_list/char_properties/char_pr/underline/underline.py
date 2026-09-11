from typing import Any, Literal, Optional
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.enums import LineType2

from hwpx_editor.values import HexColor


class Underline(BaseModel, validate_assignment=True):
    type: Optional[Literal["BOTTOM", "CENTER", "TOP"]] = Field(default=None)
    shape: LineType2 = Field(default=LineType2.SOLID)
    color: HexColor = Field(default="#000000")

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "shape": str(self.shape),
            "color": str(self.color),
        }

        if self.type is not None:
            attribs["type"] = str(self.type)

        element = etree.Element(q_name, attrib=attribs)

        return element
