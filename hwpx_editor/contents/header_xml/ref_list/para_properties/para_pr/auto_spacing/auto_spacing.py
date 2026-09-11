from typing import Any
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field


class AutoSpacing(BaseModel):
    e_asian_eng: int = Field(
        default=0,
        description="""
        한글과 영어 간격을 자동 조절 여부
        """
    )

    e_asian_num: int = Field(
        default=0,
        description="""
        한글과 숫자 간격을 자동 조절 여부
        """
    )

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "eAsianEng": str(self.e_asian_eng),
            "eAsianNum": str(self.e_asian_num),
        }

        element = etree.Element(q_name, attrib=attribs)

        return element
