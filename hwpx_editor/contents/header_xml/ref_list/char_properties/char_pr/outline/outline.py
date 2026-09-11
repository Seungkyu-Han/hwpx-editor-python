from typing import Any
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.enums import LineType1


class Outline(BaseModel):
    type: LineType1 = Field(default=LineType1.NONE)

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "type": str(self.type),
        }

        element = etree.Element(q_name, attrib=attribs)

        return element
