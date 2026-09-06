from typing import Literal, Optional

from pydantic import BaseModel, Field

from hwpx_editor.enums import NumberType1


class ParaHead(BaseModel):
    start: int = Field(default=1)
    level: int = Field(ge=0)
    align: Literal["LEFT", "RIGHT", "CENTER"] = Field(default="LEFT")
    use_inst_width: int = Field(default=1)
    auto_indent: int = Field(default=1)
    width_adjust: int = Field(default=0)
    text_offset_type: Literal["PERCENT", "HWPUNIT"] = Field(default="PERCENT")
    text_offset: int = Field(default=50)
    num_format: NumberType1 = Field(default=NumberType1.DIGIT)
    char_pr_id_ref: int = Field()
    checkable: int = Field()
    text: Optional[str] = Field(default=None)
