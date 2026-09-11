from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.trackchange_config.config_item_set import ConfigItemSet


class TrackchangeConfig(BaseModel):

    flags: int = Field(default=56)

    config_item_sets: list[ConfigItemSet] = Field(
        default_factory=lambda: [
            ConfigItemSet()
        ]
    )

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "flags": str(self.flags),
        }

        element = etree.Element(etree.QName(namespace_uri, "trackchageConfig"), attrib=attribs)

        for item in self.config_item_sets:
            element.append(item.to_xml("urn:oasis:names:tc:opendocument:xmlns:config:1.0"))

        return element
