from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.fontfaces.fontface.font import Font
from hwpx_editor.enums import Lang


class Fontface(BaseModel):
    lang: Lang = Field(description="")
    font_cnt: int = Field(default=1, description="fontCnt")
    font: list[Font] = Field(
        default_factory=lambda: [Font()],
    )