from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.trackchange_config.config_item_set.config_item import ConfigItem


class ConfigItemSet(BaseModel):

    name: str = Field(
        default="TrackChangePasswordInfo"
    )

    config_items: list[ConfigItem] = Field(
        default_factory=lambda: [
            ConfigItem(),
        ]
    )

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "name": str(self.name),
        }

        element = etree.Element(etree.QName(namespace_uri, "config-item-set"), attrib=attribs)

        q_name = etree.QName("urn:oasis:names:tc:opendocument:xmlns:config:1.0", "config-item")
        for item in self.config_items:
            element.append(item.to_xml(q_name))

        return element
