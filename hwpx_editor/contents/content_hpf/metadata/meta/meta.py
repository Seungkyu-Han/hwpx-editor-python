from typing import Any, Optional
from xml.etree.ElementTree import QName

from lxml import etree
from pydantic import BaseModel, Field


class Meta(BaseModel):
    name: str
    content: str = Field(default="text")
    text: Optional[str] = None

    def to_xml(self, q_name: QName) -> Any:

        attribs: dict[str, str] = {
            "name": self.name,
            "content": self.content,
        }

        element = etree.Element(
            q_name,
            attrib=attribs,
        )

        if self.text is not None:
            element.text = self.text

        return element