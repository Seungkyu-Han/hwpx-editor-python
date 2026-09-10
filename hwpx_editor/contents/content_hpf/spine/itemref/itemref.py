from typing import Any
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field


class Itemref(BaseModel):
    idref: str = Field()
    linear: str = Field(default="yes")

    def to_xml(self, q_name: QName) -> Any:
        attribs: dict[str, str] = {
            "idref": self.idref,
            "linear": self.linear,
        }

        return etree.Element(
            q_name,
            attrib=attribs,
        )
