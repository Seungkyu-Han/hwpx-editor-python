from typing import Any
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field


class ForbiddenWord(BaseModel):

    text: str = Field(
        description="""
        금칙 문자
        요소의 값으로 문자열을 가짐.
        """
    )

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
        }

        element = etree.Element(q_name, attrib=attribs)

        element.text = self.text

        return element
