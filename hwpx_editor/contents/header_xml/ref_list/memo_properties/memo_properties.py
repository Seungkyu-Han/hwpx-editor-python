from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.memo_properties.memo_pr import MemoPr


class MemoProperties(BaseModel):
    item_cnt: int = Field(default=0)

    memo_properties: list[MemoPr] = Field(default_factory=lambda: [])
