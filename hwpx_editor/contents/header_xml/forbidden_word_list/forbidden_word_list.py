from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.forbidden_word_list.forbidden_word import ForbiddenWord


class ForbiddenWordList(BaseModel):
    item_cnt: int = Field(default=0)

    forbidden_words: list[ForbiddenWord] = Field(
        default_factory=lambda: []
    )
