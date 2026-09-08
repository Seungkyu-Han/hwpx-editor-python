from typing import Literal

from pydantic import BaseModel, Field


class Style(BaseModel):
    id: int = Field(
        ge=0,
    )

    type: Literal["PARA", "CHAR"] = Field()

    name: str = Field()

    eng_name: str = Field()

    para_pr_id_ref: int = Field()

    char_pr_id_ref: int = Field()

    next_style_id_ref: int = Field()

    lang_id: int = Field(default=1042)

    lock_form: int = Field(default=0)