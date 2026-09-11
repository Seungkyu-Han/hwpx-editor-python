from typing import Any, Literal

from lxml import etree
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

from hwpx_editor.values import HexColor


class CharPr(BaseModel, validate_assignment=True):

    id: int = Field()
    height: int = Field()
    text_color: HexColor = Field(description="textColor")
    shade_color: HexColor | Literal["none"] = Field(default="none")
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

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "id": str(self.id),
            "height": str(self.height),
            "textColor": str(self.text_color),
            "shadeColor": str(self.shade_color),
            "useFontSpace": str(self.use_font_space),
            "useKerning": str(self.use_kerning),
            "symMark": str(self.sym_mark),
            "borderFillIDRef": str(self.border_fill_id_ref),
        }

        element = etree.Element(etree.QName(namespace_uri, "charPr"), attrib=attribs)

        q_name = etree.QName(namespace_uri, "fontRef")
        element.append(self.font_ref.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "ratio")
        element.append(self.ratio.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "spacing")
        element.append(self.spacing.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "relSz")
        element.append(self.rel_sz.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "offset")
        element.append(self.offset.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "underline")
        element.append(self.underline.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "strikeout")
        element.append(self.strikeout.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "outline")
        element.append(self.outline.to_xml(q_name))

        q_name = etree.QName(namespace_uri, "shadow")
        element.append(self.shadow.to_xml(q_name))

        return element
