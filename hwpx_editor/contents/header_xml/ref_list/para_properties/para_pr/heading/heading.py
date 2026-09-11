from typing import Any, Literal
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field


class Heading(BaseModel):
    type: Literal["NONE", "OUTLINE", "NUMBER", "BULLET"] = Field(
        default="NONE",
        description="""
        문단 머리 모양 종류
        NONE: 없음
        OUTLINE: 개요
        NUMBER: 번호
        """
    )

    id_ref: int = Field(
        default=0,
        ge=0,
        description="""
        문단 머리 번호/글머리표 모양 아이디 참조값
        """
    )

    level: int = Field(
        default=0,
        ge=0,
        description="""
        참조 단계
        """
    )

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "type": str(self.type),
            "idRef": str(self.id_ref),
            "level": str(self.level),
        }

        element = etree.Element(q_name, attrib=attribs)

        return element
