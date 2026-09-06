from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.content_hpf.manifest import Manifest
from hwpx_editor.contents.content_hpf.metadata import Metadata
from hwpx_editor.contents.content_hpf.spine import Spine


class ContentHPF(BaseModel):
    metadata: Metadata = Field(default_factory=Metadata)
    manifest: Manifest = Field(default_factory=Manifest)
    spine: Spine = Field(default_factory=Spine)

    _namespaces: dict[str, str] = {
        "ha": "http://www.hancom.co.kr/hwpml/2011/app",
        "hp": "http://www.hancom.co.kr/hwpml/2011/paragraph",
        "hp10": "http://www.hancom.co.kr/hwpml/2016/paragraph",
        "hs": "http://www.hancom.co.kr/hwpml/2011/section",
        "hc": "http://www.hancom.co.kr/hwpml/2011/core",
        "hh": "http://www.hancom.co.kr/hwpml/2011/head",
        "hhs": "http://www.hancom.co.kr/hwpml/2011/history",
        "hm": "http://www.hancom.co.kr/hwpml/2011/master-page",
        "hpf": "http://www.hancom.co.kr/schema/2011/hpf",
        "dc": "http://purl.org/dc/elements/1.1/",
        "opf": "http://www.idpf.org/2007/opf/",
        "ooxmlchart": "http://www.hancom.co.kr/hwpml/2016/ooxmlchart",
        "hwpunitchar": "http://www.hancom.co.kr/hwpml/2016/HwpUnitChar",
        "epub": "http://www.idpf.org/2007/ops",
        "config": "urn:oasis:names:tc:opendocument:xmlns:config:1.0",
    }

    @property
    def xml(self) -> Any:
        opf_uri = self._namespaces["opf"]

        root = etree.Element(
            etree.QName(opf_uri, "package"),
            nsmap=self._namespaces,
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
