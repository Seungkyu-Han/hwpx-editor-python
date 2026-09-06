from typing import Literal

from pydantic import BaseModel, Field

from hwpx_editor.enums import LineType2


class TabItem(BaseModel):
    pos: int = Field()
    type: Literal["LEFT", "RIGHT", "CENTER", "DECIMAL"] = Field()
    leader: LineType2 = Field()