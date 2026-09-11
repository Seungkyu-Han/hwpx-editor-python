from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.border_fills.border_fill.fill_brush.win_brush import WinBrush


class FillBrush(BaseModel):
    win_brush: WinBrush = Field(default_factory=lambda: WinBrush())

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
        }

        element = etree.Element(etree.QName(namespace_uri, "fillBrush"), attrib=attribs)

        q_name = etree.QName("http://www.hancom.co.kr/hwpml/2011/core", "winBrush")
        element.append(self.win_brush.to_xml(q_name))

        return element
