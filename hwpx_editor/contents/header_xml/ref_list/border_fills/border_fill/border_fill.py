from typing import Any, Optional

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.border_fills.border_fill.back_slash import BackSlash
from hwpx_editor.contents.header_xml.ref_list.border_fills.border_fill.bottom_border import BottomBorder
from hwpx_editor.contents.header_xml.ref_list.border_fills.border_fill.diagonal import Diagonal
from hwpx_editor.contents.header_xml.ref_list.border_fills.border_fill.fill_brush import FillBrush
from hwpx_editor.contents.header_xml.ref_list.border_fills.border_fill.left_border import LeftBorder
from hwpx_editor.contents.header_xml.ref_list.border_fills.border_fill.right_border import RightBorder
from hwpx_editor.contents.header_xml.ref_list.border_fills.border_fill.slash import Slash
from hwpx_editor.contents.header_xml.ref_list.border_fills.border_fill.top_border import TopBorder


class BorderFill(BaseModel):

    id: int = Field(ge=0)
    three_d: int = Field(default=0, ge=0, le=1)
    shadow: int = Field(default=0, ge=0, le=1)
    center_line: str = Field(default="NONE")
    break_cell_separate_line: int = Field(default=0, ge=0, le=1)

    slash: Slash = Field(default_factory=lambda: Slash())
    back_slash: BackSlash = Field(default_factory=lambda: BackSlash(), description="backSlash")
    left_border: LeftBorder = Field(default_factory=lambda: LeftBorder())
    right_border: RightBorder = Field(default_factory=lambda: RightBorder())
    top_border: TopBorder = Field(default_factory=lambda: TopBorder())
    bottom_border: BottomBorder = Field(default_factory=lambda: BottomBorder())
    diagonal: Diagonal = Field(default_factory=lambda: Diagonal())
    fill_brush: Optional[FillBrush] = Field(default=None)

    def to_xml(self, namespace_uri: str, hc_namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "id": str(self.id),
            "threeD": str(self.three_d),
            "shadow": str(self.shadow),
            "centerLine": str(self.center_line),
            "breakCellSeparateLine": str(self.break_cell_separate_line),
        }

        element = etree.Element(etree.QName(namespace_uri, "borderFill"), attrib=attribs)

        q_name = etree.QName(namespace_uri, "slash")
        element.append(self.slash.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "backSlash")
        element.append(self.back_slash.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "leftBorder")
        element.append(self.left_border.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "rightBorder")
        element.append(self.right_border.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "topBorder")
        element.append(self.top_border.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "bottomBorder")
        element.append(self.bottom_border.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "diagonal")
        element.append(self.diagonal.to_xml(q_name))

        if self.fill_brush is not None:
            element.append(self.fill_brush.to_xml(hc_namespace_uri))

        return element
