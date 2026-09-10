from lxml.etree import QName

from lxml import etree
from typing import Any, Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    id: str = Field()
    href: str = Field()
    media_type: str = Field(description="media-type")
    is_embedded: Optional[int] = Field(default=None, description="isEmbedded")
    sub_path: Optional[str] = Field(default=None, description="sub-path")

    def to_xml(self, q_name: QName) -> Any:

        attribs: dict[str, str] = {
            "id": self.id,
            "href": self.href,
            "media-type": self.media_type,
        }

        if self.is_embedded is not None:
            attribs["isEmbeded"] = str(self.is_embedded)

        if self.sub_path is not None:
            attribs["sub-path"] = self.sub_path

        return etree.Element(
            q_name,
            attrib=attribs,
        )