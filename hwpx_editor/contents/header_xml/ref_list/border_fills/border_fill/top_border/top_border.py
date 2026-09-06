from pydantic import BaseModel, Field

from hwpx_editor.enums import LineType2


class TopBorder(BaseModel):
    type: LineType2 = Field(default=LineType2.NONE)
    width: float = Field(default=0.12)
    color: str = Field(default="#000000")