from typing import Optional

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