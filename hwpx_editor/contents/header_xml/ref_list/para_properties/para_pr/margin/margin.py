from typing import Any
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.values import HWPValue


class Margin(BaseModel):
    intent: HWPValue = Field(
        default_factory=lambda: HWPValue(),
        description="""
        들여쓰기/내어쓰기
        n이 0보다 크면 들여쓰기 n
        n이 0이면 보통
        n이 0보다 작으면 내어쓰기 N
        """,
    )

    left: HWPValue = Field(
        default_factory=lambda: HWPValue(),
        description="""
        왼쪽 여백
        """,
    )

    right: HWPValue = Field(
        default_factory=lambda: HWPValue(),
        description="""
            오른쪽 여백
            """,
    )

    prev: HWPValue = Field(
        default_factory=lambda: HWPValue(),
        description="""
            위쪽 문단 간격
            """,
    )

    next: HWPValue = Field(
        default_factory=lambda: HWPValue(),
        description="""
            아래쪽 문단 간격
            """,
    )

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
        }

        element = etree.Element(q_name, attrib=attribs)

        etree.SubElement(element, etree.QName("http://www.hancom.co.kr/hwpml/2011/core", "intent"), attrib={
            "value": str(self.intent.value),
            "unit": str(self.intent.unit),
        })

        etree.SubElement(element, etree.QName("http://www.hancom.co.kr/hwpml/2011/core", "left"), attrib={
            "value": str(self.left.value),
            "unit": str(self.left.unit),
        })

        etree.SubElement(element, etree.QName("http://www.hancom.co.kr/hwpml/2011/core", "right"), attrib={
            "value": str(self.right.value),
            "unit": str(self.right.unit),
        })

        etree.SubElement(element, etree.QName("http://www.hancom.co.kr/hwpml/2011/core", "prev"), attrib={
            "value": str(self.prev.value),
            "unit": str(self.prev.unit),
        })

        etree.SubElement(element, etree.QName("http://www.hancom.co.kr/hwpml/2011/core", "next"), attrib={
            "value": str(self.next.value),
            "unit": str(self.next.unit),
        })

        return element
