from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.fontfaces import FontFaces
from hwpx_editor.contents.header_xml.ref_list.border_fills import BorderFills
from hwpx_editor.contents.header_xml.ref_list.char_properties import CharProperties
from hwpx_editor.contents.header_xml.ref_list.tab_properties import TabProperties
from hwpx_editor.contents.header_xml.ref_list.numberings import Numberings
from hwpx_editor.contents.header_xml.ref_list.bullets import Bullets
from hwpx_editor.contents.header_xml.ref_list.para_properties import ParaProperties
from hwpx_editor.contents.header_xml.ref_list.styles import Styles
from hwpx_editor.contents.header_xml.ref_list.memo_properties import MemoProperties
from hwpx_editor.contents.header_xml.ref_list.track_changes import TrackChanges
from hwpx_editor.contents.header_xml.ref_list.track_change_authors import TrackChangeAuthors


class RefList(BaseModel):
    fontfaces: FontFaces = Field(default_factory=FontFaces)
    border_fills: BorderFills = Field(default_factory=BorderFills)
    char_properties: CharProperties = Field(default_factory=CharProperties)
    tab_properties: TabProperties = Field(default_factory=TabProperties)
    numberings: Numberings = Field(default_factory=Numberings)
    bullets: Bullets | None = Field(default=None)
    para_properties: ParaProperties = Field(default_factory=ParaProperties)
    styles: Styles = Field(default_factory=Styles)
    memo_properties: MemoProperties | None = Field(default=None)
    track_changes: TrackChanges | None = Field(default=None)
    track_change_authors: TrackChangeAuthors | None = Field(default=None)

    def to_xml(self, namespace_uri: str, hc_namespace_uri: str) -> etree._Element:
        element = etree.Element(etree.QName(namespace_uri, "refList"))
        element.append(self.fontfaces.to_xml(namespace_uri))
        element.append(self.border_fills.to_xml(namespace_uri, hc_namespace_uri))
        element.append(self.char_properties.to_xml(namespace_uri))
        element.append(self.tab_properties.to_xml(namespace_uri))
        element.append(self.numberings.to_xml(namespace_uri))
        if self.bullets is not None:
            element.append(self.bullets.to_xml(namespace_uri))
        element.append(self.para_properties.to_xml(namespace_uri))
        element.append(self.styles.to_xml(namespace_uri))
        if self.memo_properties is not None:
            element.append(self.memo_properties.to_xml(namespace_uri))
        if self.track_changes is not None:
            element.append(self.track_changes.to_xml(namespace_uri))
        if self.track_change_authors is not None:
            element.append(self.track_change_authors.to_xml(namespace_uri))
        return element
