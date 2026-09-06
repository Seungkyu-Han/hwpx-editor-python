from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.border_fills.border_fill.fill_brush.win_brush import WinBrush


class FillBrush(BaseModel):
    win_brush: WinBrush = Field(default_factory=lambda: WinBrush())