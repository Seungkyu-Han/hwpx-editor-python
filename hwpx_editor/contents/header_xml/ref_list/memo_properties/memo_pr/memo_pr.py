from pydantic import BaseModel, Field

from hwpx_editor.enums import LineType2


class MemoPr(BaseModel):

    id: int = Field(
        ge=0,
    )

    width: int = Field(
        ge=0,
    )

    line_type: LineType2 = Field(
        default=LineType2.SOLID,
    )

    line_color: str = Field()

    fill_color: str = Field()

    active_color: str = Field()

    memo_type: str = Field()

    line_width: int = Field()