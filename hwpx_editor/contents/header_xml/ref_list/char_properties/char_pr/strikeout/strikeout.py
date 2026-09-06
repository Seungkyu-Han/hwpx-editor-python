from pydantic import BaseModel
from pydantic.v1 import Field

from hwpx_editor.enums import LineType2


class Strikeout(BaseModel):
    type: LineType2 = Field(default=LineType2.NONE)
    color: str = Field(default="#000000")