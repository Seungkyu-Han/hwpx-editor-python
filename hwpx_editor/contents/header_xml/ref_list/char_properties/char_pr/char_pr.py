from pydantic import Field, BaseModel

from hwpx_editor.contents.header_xml.ref_list.char_properties.char_pr.font_ref import FontRef
from hwpx_editor.contents.header_xml.ref_list.char_properties.char_pr.offset.offset import Offset
from hwpx_editor.contents.header_xml.ref_list.char_properties.char_pr.outline import Outline
from hwpx_editor.contents.header_xml.ref_list.char_properties.char_pr.ratio import Ratio
from hwpx_editor.contents.header_xml.ref_list.char_properties.char_pr.rel_sz import RelSz
from hwpx_editor.contents.header_xml.ref_list.char_properties.char_pr.shadow import Shadow
from hwpx_editor.contents.header_xml.ref_list.char_properties.char_pr.spacing import Spacing
from hwpx_editor.contents.header_xml.ref_list.char_properties.char_pr.strikeout.strikeout import Strikeout
from hwpx_editor.contents.header_xml.ref_list.char_properties.char_pr.underline import Underline


class CharPr(BaseModel):

    id: int = Field()
    height: int = Field()
    text_color: str = Field(description="textColor")
    shade_color: str = Field(default="none")
    use_font_space: int = Field(default=0)
    use_kerning: int = Field(default=0)
    sym_mark: str = Field(default="NONE")
    border_fill_id_ref: int = Field(default=2)

    font_ref: FontRef = Field(default_factory=lambda: FontRef())
    ratio: Ratio = Field(default_factory=lambda: Ratio())
    spacing: Spacing = Field(default_factory=lambda: Spacing())
    rel_sz: RelSz = Field(default_factory=lambda: RelSz())
    offset: Offset = Field(default_factory=lambda: Offset())
    underline: Underline = Field(default_factory=lambda: Underline())
    strikeout: Strikeout = Field(default_factory=lambda: Strikeout())
    outline: Outline = Field(default_factory=lambda: Outline())
    shadow: Shadow = Field(default_factory=lambda: Shadow())
