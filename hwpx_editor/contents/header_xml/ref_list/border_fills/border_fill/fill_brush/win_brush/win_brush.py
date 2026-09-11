from typing import Any, Literal
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.values import HexColor


class WinBrush(BaseModel, validate_assignment=True):
    face_color: HexColor | Literal["none"] = Field(default="none")
    hatch_color: HexColor = Field(default="#999999")
    alpha: float = Field(default=0, description="투명도")

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "faceColor": str(self.face_color),
            "hatchColor": str(self.hatch_color),
            "alpha": str(self.alpha),
        }

        element = etree.Element(q_name, attrib=attribs)

        return element
