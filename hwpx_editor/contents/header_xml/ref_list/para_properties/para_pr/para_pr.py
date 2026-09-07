from typing import Literal

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