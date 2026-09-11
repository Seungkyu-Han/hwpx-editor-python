from datetime import datetime
from typing import Any, Literal
from lxml.etree import QName

from lxml import etree

from pydantic import BaseModel, Field


class TrackChange(BaseModel):

    type: Literal[
        "UnKnown",
        "Insert",
        "Delete",
        "CharShape",
        "ParaShape",
    ] = Field(
        description="""
        변경 추적의 종류
        UnKnown: 없음
        Insert: 삽입
        Delete: 삭제
        CharShape: 글자 서식 변경
        ParaShape: 문단 서식 변경
        """
    )

    date: datetime = Field(
        default_factory=datetime.now,
    )

    author_id: int = Field(
        ge=0,
        description="""
        변경 추적 검토자를 구별하기 위한 아이디
        """
    )

    char_shape_id: int = Field(
        ge=0,
        description="""
        변경 추적 글자의 서식 정보
        """
    )

    para_shape_id: int = Field(
        ge=0,
        description="""
        변경 추적 문단의 서식 정보
        """
    )

    hide: int = Field(
        default=0,
    )

    id: int = Field(
        ge=0,
    )

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "type": str(self.type),
            "date": self.date.isoformat(),
            "authorID": str(self.author_id),
            "charShapeID": str(self.char_shape_id),
            "paraShapeID": str(self.para_shape_id),
            "hide": str(self.hide),
            "id": str(self.id),
        }

        element = etree.Element(q_name, attrib=attribs)

        return element
