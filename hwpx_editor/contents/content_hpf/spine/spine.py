from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.content_hpf.spine.itemref import Itemref


class Spine(BaseModel):

    header: Itemref = Field(default_factory= lambda: Itemref(idref="header", linear="yes"))
    section0: Itemref = Field(default_factory= lambda: Itemref(idref="section0", linear="yes"))
    headersc: Itemref = Field(default_factory= lambda: Itemref(idref="headersc", linear="yes"))
    sourcesc: Itemref = Field(default_factory= lambda: Itemref(idref="sourcesc", linear="yes"))

    def to_xml(self, opf_uri: str) -> Any:

        spine_element = etree.Element(etree.QName(opf_uri, "spine"))

        q_name = etree.QName(opf_uri, "itemref")

        for itemref in (self.header, self.section0, self.headersc, self.sourcesc):
            spine_element.append(itemref.to_xml(q_name))

        return spine_element