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