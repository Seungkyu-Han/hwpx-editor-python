from typing import Any
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.enums import LineType2

from hwpx_editor.values import HexColor


class MemoPr(BaseModel, validate_assignment=True):

    id: int = Field(
        ge=0,
    )

    width: int = Field(
        ge=0,
    )

    line_type: LineType2 = Field(
        default=LineType2.SOLID,
    )

    line_color: HexColor = Field()

    fill_color: HexColor = Field()

    active_color: HexColor = Field()

    memo_type: str = Field()

    line_width: int = Field()

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "id": str(self.id),
            "width": str(self.width),
            "lineType": str(self.line_type),
            "lineColor": str(self.line_color),
            "fillColor": str(self.fill_color),
            "activeColor": str(self.active_color),
            "memoType": str(self.memo_type),
            "lineWidth": str(self.line_width),
        }

        element = etree.Element(q_name, attrib=attribs)

        return element
