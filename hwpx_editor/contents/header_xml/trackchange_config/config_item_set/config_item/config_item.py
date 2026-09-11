from typing import Any
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field


class ConfigItem(BaseModel):
    name: str = Field(
        default="algorithm-name"
    )

    type: str = Field(
        default="string"
    )

    text: str = Field(
        default="SHA1"
    )

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "name": str(self.name),
            "type": str(self.type),
        }

        element = etree.Element(q_name, attrib=attribs)

        element.text = self.text

        return element
