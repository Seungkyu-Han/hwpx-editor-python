from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.border_fills.border_fill import BorderFill
from hwpx_editor.contents.header_xml.ref_list.border_fills.border_fill.fill_brush import FillBrush


class BorderFills(BaseModel):
    item_cnt: int = Field(default=2)

    border_fills: list[BorderFill] = Field(
        default_factory=lambda: [
            BorderFill(
                id=1,
            ),
            BorderFill(
                id=2,
                fill_brush=FillBrush(),
            ),
        ],
    )

    def to_xml(self, namespace_uri: str, hc_namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "itemCnt": str(self.item_cnt),
        }

        element = etree.Element(etree.QName(namespace_uri, "borderFills"), attrib=attribs)

        for item in self.border_fills:
            element.append(item.to_xml(namespace_uri, hc_namespace_uri))

        return element
