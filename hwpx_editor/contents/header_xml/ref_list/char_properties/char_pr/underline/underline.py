from typing import Literal, Optional

from pydantic import BaseModel, Field

from hwpx_editor.enums import LineType2


class Underline(BaseModel):
    type: Optional[Literal["BOTTOM", "CENTER", "TOP"]] = Field(default=None)
    shape: LineType2 = Field(default=LineType2.SOLID)
    color: str = Field(default="#000000")