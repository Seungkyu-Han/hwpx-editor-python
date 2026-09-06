from pydantic import BaseModel, Field

from hwpx_editor.enums import LineType1


class Outline(BaseModel):
    type: LineType1 = Field(default=LineType1.NONE)