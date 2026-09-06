from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.numberings.numbering import Numbering


class Numberings(BaseModel):

    item_cnt: int = Field(default=1)

    numberings: list[Numbering] = Field(
        default_factory=lambda: [Numbering()],
    )