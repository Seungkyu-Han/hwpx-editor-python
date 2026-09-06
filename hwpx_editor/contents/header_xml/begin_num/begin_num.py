from typing import Any
from xml.etree.ElementTree import QName

from lxml import etree
from pydantic import BaseModel, Field


class BeginNum(BaseModel):
    page: int = Field(default=1, description="페이지 시작 번호")
    footnote: int = Field(default=1, description="각주 시작 번호")
    endnote: int = Field(default=1, description="미주 시작 번호")
    pic: int = Field(default=1, description="그림 시작 번호")
    tbl: int = Field(default=1, description="표 시작 번호")
    equation: int = Field(default=1, description="수식 시작 번호")

    def to_xml(self, q_name: QName) -> Any:

        attribs: dict[str, str] = {
            "page": str(self.page),
            "footnote": str(self.footnote),
            "endnote": str(self.endnote),
            "pic": str(self.pic),
            "tbl": str(self.tbl),
            "equation": str(self.equation),
        }

        return etree.Element(
            q_name,
            attrib=attribs,
        )