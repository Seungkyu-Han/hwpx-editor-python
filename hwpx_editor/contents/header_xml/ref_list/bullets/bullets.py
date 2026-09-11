from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.bullets.bullet import Bullet


class Bullets(BaseModel):

    item_cnt: int = Field(default=1)

    bullets: list[Bullet] = Field(
        default_factory=lambda: [Bullet(
            id=1,
        )],
    )

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "itemCnt": str(self.item_cnt),
        }

        element = etree.Element(etree.QName(namespace_uri, "bullets"), attrib=attribs)

        for item in self.bullets:
            element.append(item.to_xml(namespace_uri))

        return element
