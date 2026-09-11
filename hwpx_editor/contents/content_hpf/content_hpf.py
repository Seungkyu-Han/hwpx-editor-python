from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.content_hpf.manifest import Manifest
from hwpx_editor.contents.content_hpf.metadata import Metadata
from hwpx_editor.contents.content_hpf.spine import Spine
from hwpx_editor.namespaces import namespaces


class ContentHPF(BaseModel):
    metadata: Metadata = Field(default_factory=Metadata)
    manifest: Manifest = Field(default_factory=Manifest)
    spine: Spine = Field(default_factory=Spine)

    @property
    def xml(self) -> Any:
        opf_uri = namespaces["opf"]

        root = etree.Element(
            etree.QName(opf_uri, "package"),
            nsmap=namespaces,
            attrib={"version": "", "unique-identifier": "", "id": ""},
        )

        for component in (self.metadata, self.manifest, self.spine):
            root.append(component.to_xml(opf_uri))

        xml_bytes = etree.tostring(
            root, xml_declaration=True, encoding="UTF-8", pretty_print=True
        )
        xml_str = xml_bytes.decode("utf-8")

        return xml_str.replace(
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        )
