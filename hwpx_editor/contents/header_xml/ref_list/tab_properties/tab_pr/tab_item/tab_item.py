from typing import Any, Literal
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.enums import LineType2


class TabItem(BaseModel):
    pos: int = Field()
    type: Literal["LEFT", "RIGHT", "CENTER", "DECIMAL"] = Field()
    leader: LineType2 = Field()

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "pos": str(self.pos),
            "type": str(self.type),
            "leader": str(self.leader),
        }

        element = etree.Element(q_name, attrib=attribs)

        return element
