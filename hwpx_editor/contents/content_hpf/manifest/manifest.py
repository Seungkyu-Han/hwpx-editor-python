from typing import Optional, Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.content_hpf.manifest.item import Item


class Manifest(BaseModel):
    header: Item = Field(
        default=Item(id="header", href="Contents/header.xml", media_type="application/xml", is_embedded=None, sub_path=None)
    )

    sections: list[Item] = Field(default_factory=lambda: [Item(id="section0", href="Contents/section0.xml", media_type="application/xml", is_embedded=None, sub_path=None)])

    images: list[Item] = Field(default_factory=list)

    headersc: Item = Field(
        default_factory=lambda: Item(id="headersc", href="Scripts/headerScripts", media_type="application/x-javascript ;charset=utf-16", is_embedded=None, sub_path=None)
    )

    sourcesc: Item = Field(
        default_factory=lambda: Item(id="sourcesc", href="Scripts/sourceScripts", media_type="application/x-javascript ;charset=utf-16", is_embedded=None, sub_path=None)
    )

    settings: Item = Field(
        default_factory=lambda: Item(id="settings", href="settings.xml", media_type="application/xml", is_embedded=None, sub_path=None)
    )

    _section_pointer: int = 0
    _image_pointer: int = 0

    def add_section(self):
        self._section_pointer += 1
        section_id = self._section_pointer
        self.sections.append(Item(id=f"section{section_id}", href=f"Contents/section{section_id}.xml", media_type="application/xml", is_embedded=None, sub_path=None))
        return self.sections[-1]

    def remove_section(self, id_: Optional[int] = None) -> Item:

        section_id = f'section{id_}' if id_ else f'section{self._section_pointer}'

        for section in self.sections:
            if section.id == section_id:
                self.sections.remove(section)
                return section

        raise ValueError(f"Section with id {section_id} not found")

    def add_image(self):
        self._image_pointer += 1
        image_id = self._image_pointer
        self.images.append(Item(id=f"image{image_id}", href=f"BinData/image{image_id}.png", media_type="image/png", is_embedded=1, sub_path=None))
        return self.images[-1]

    def remove_image(self, id_: Optional[int] = None) -> Item:

        image_id = f'image{id_}' if id_ else f'image{self._image_pointer}'

        for image in self.images:
            if image.id == image_id:
                self.images.remove(image)
                return image

        raise ValueError(f"Image with id {image_id} not found")

    def to_xml(self, opf_uri: str) -> Any:

        manifest_element = etree.Element(etree.QName(opf_uri, "manifest"))

        q_name = etree.QName(opf_uri, "item")

        for item in (self.header, *self.sections, *self.images, self.headersc, self.sourcesc, self.settings):
            manifest_element.append(item.to_xml(q_name))

        return manifest_element