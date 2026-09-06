from typing import Optional

from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.tab_properties.tab_pr.tab_item import TabItem


class TabPr(BaseModel):
    id: int = Field()
    auto_tab_left: int = Field()
    auto_tab_right: int = Field()

    tab_item: Optional[TabItem] = Field(default=None)