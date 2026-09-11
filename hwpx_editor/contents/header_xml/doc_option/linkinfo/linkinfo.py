from typing import Any
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field


class LinkInfo(BaseModel):
    path: str = Field(default="")
    page_inherit: int = Field(default=0)
    footnote_inherit: int = Field(default=0)

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "path": str(self.path),
            "pageInherit": str(self.page_inherit),
            "footnoteInherit": str(self.footnote_inherit),
        }

        element = etree.Element(q_name, attrib=attribs)

        return element
