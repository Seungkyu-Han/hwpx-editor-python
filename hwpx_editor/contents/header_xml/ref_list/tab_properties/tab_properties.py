from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.tab_properties.tab_pr import TabPr


class TabProperties(BaseModel):

    item_cnt: int = Field(default=3)

    tab_prs: list[TabPr] = Field(
        default_factory=lambda: [
            TabPr(id = 0, auto_tab_left = 0, auto_tab_right = 0),
            TabPr(id = 1, auto_tab_left = 1, auto_tab_right = 0),
            TabPr(id = 2, auto_tab_left = 0, auto_tab_right = 1),
        ]
    )