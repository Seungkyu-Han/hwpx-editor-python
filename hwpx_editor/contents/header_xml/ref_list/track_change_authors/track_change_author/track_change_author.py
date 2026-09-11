from typing import Any, Optional
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.values import HexColor


class TrackChangeAuthor(BaseModel, validate_assignment=True):
    name: str = Field(
        description="검토자 이름"
    )

    mark: int = Field(
        description="검토 표시 여부"
    )

    color: Optional[HexColor] = Field(
        description="검토 표시 색상"
    )

    id: int = Field(
        description="검토자를 구별하기 위한 아이디"
    )

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "name": str(self.name),
            "mark": str(self.mark),
            "id": str(self.id),
        }

        if self.color is not None:
            attribs["color"] = str(self.color)

        element = etree.Element(q_name, attrib=attribs)

        return element
