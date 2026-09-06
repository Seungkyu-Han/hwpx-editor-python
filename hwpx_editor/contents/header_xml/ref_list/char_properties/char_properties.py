from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.char_properties.char_pr import CharPr


class CharProperties(BaseModel):
    item_cnt: int = Field(default=5)
    char_prs: list[CharPr] = Field(
        default_factory=lambda: [
            CharPr(
                id=0,
                height=1000,
                text_color="#000000",
            ),
            CharPr(
                id=1,
                height=900,
                text_color="#000000",
            ),
            CharPr(
                id=2,
                height=900,
                text_color="#000000",
            ),
            CharPr(
                id=3,
                height=1600,
                text_color="#2E74B5",
            ),
            CharPr(
                id=4,
                height=1100,
                text_color="#000000",
            ),
        ]
    )
