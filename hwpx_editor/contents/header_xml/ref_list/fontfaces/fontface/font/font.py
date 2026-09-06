from typing import Optional

from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.fontfaces.fontface.font.type_info import TypeInfo


class Font(BaseModel):
    id: int = Field(default=0)
    face: str = Field(default="맑은 고딕")
    type: str = Field(default="TTF")
    is_embedded: int = Field(default=0)
    binary_item_id_ref: Optional[int] = Field(default=None)
    type_info: TypeInfo = Field(default_factory=lambda: TypeInfo())
