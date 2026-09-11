from typing import Any, Literal

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.para_properties.para_pr.align import Align
from hwpx_editor.contents.header_xml.ref_list.para_properties.para_pr.auto_spacing import AutoSpacing
from hwpx_editor.contents.header_xml.ref_list.para_properties.para_pr.border import Border
from hwpx_editor.contents.header_xml.ref_list.para_properties.para_pr.break_setting import BreakSetting
from hwpx_editor.contents.header_xml.ref_list.para_properties.para_pr.heading import Heading
from hwpx_editor.contents.header_xml.ref_list.para_properties.para_pr.line_spacing import LineSpacing
from hwpx_editor.contents.header_xml.ref_list.para_properties.para_pr.margin import Margin


class ParaPr(BaseModel):
    id: int = Field()
    tab_pr_id_ref: int = Field(
        default=0,
        description="탭 정의 아이디 참조값",
    )
    condense: int = Field(
        default=0,
        description="공백 최소값. 단위는 %",
    )
    font_line_height: int = Field(
        default=0,
        description="글꼴에 어울리는 줄 높이 사용 여부",
    )
    snap_to_grid: int = Field(
        default=1,
        description="편집 용지의 줄 격자 사용 여부",
    )
    suppress_line_numbers: int = Field(
        default=0,
        description="줄 번호 건너뜀 사용 여부",
    )
    checked: int = Field(
        default=0,
        description="선택 글머리표 여부",
    )
    text_dir: Literal["RTL", "LTR"] = Field(
        default="LTR",
        description="""
        문단 방향 정보
        RTL: 오른쪽에서 왼쪽
        LTR: 왼쪽에서 오른쪽
        """
    )

    align: Align = Field(default_factory=lambda: Align())
    heading: Heading = Field(default_factory=lambda: Heading())
    break_setting: BreakSetting = Field(default_factory=lambda: BreakSetting())
    auto_spacing: AutoSpacing = Field(default_factory=lambda: AutoSpacing())
    border: Border = Field(default_factory=lambda: Border())
    margin: Margin = Field(default_factory=lambda: Margin())
    line_spacing: LineSpacing = Field(default_factory=lambda: LineSpacing())

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "id": str(self.id),
            "tabPrIDRef": str(self.tab_pr_id_ref),
            "condense": str(self.condense),
            "fontLineHeight": str(self.font_line_height),
            "snapToGrid": str(self.snap_to_grid),
            "suppressLineNumbers": str(self.suppress_line_numbers),
            "checked": str(self.checked),
            "textDir": str(self.text_dir),
        }

        element = etree.Element(etree.QName(namespace_uri, "paraPr"), attrib=attribs)

        q_name = etree.QName(namespace_uri, "align")
        element.append(self.align.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "heading")
        element.append(self.heading.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "breakSetting")
        element.append(self.break_setting.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "autoSpacing")
        element.append(self.auto_spacing.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "margin")
        element.append(self.margin.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "lineSpacing")
        element.append(self.line_spacing.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "border")
        element.append(self.border.to_xml(q_name))

        return element
