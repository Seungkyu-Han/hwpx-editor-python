from typing import Any
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field


class FontRef(BaseModel):
    hangul: int = Field(default=0)
    latin: int = Field(default=0)
    hanja: int = Field(default=0)
    japanese: int = Field(default=0)
    other: int = Field(default=0)
    symbol: int = Field(default=0)
    user: int = Field(default=0)

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "hangul": str(self.hangul),
            "latin": str(self.latin),
            "hanja": str(self.hanja),
            "japanese": str(self.japanese),
            "other": str(self.other),
            "symbol": str(self.symbol),
            "user": str(self.user),
        }

        element = etree.Element(q_name, attrib=attribs)

        return element
