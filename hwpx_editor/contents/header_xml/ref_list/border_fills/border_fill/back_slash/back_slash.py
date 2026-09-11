from typing import Any
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.enums import SlashType

class BackSlash(BaseModel):
    type: SlashType = Field(
        default=SlashType.NONE,
        description="""
        BackSlash 모양
        NONE: 없음
        CENTER: 중심선만
        CENTER_BELOW: 중심선 + 중심선 아래선
        CENTER_ABOVE: 중심선 + 중심선 위선
        ALL: 중심선 + 아래선 + 위선
        """,
    )

    crooked: int = Field(
        default=0,
        description="""
        꺾인 대각선
        BackSlash의 가운데 대각선이 꺾인 대각선임을 나타냄
        """
    )

    is_counter: int = Field(
        default=0,
        description="""
        BackSlash 대각선의 역방향 여부
        """
    )

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "type": str(self.type),
            "Crooked": str(self.crooked),
            "isCounter": str(self.is_counter),
        }

        element = etree.Element(q_name, attrib=attribs)

        return element
