from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.bullets.bullet.para_head import ParaHead


class Bullet(BaseModel):
    id: int = Field()
    char: str = Field(default="a")
    use_image: int = Field(default=0)

    para_head: ParaHead = Field(default_factory=lambda: ParaHead(level=0, char_pr_id_ref=4294967295, checkable=0))

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "id": str(self.id),
            "char": str(self.char),
            "useImage": str(self.use_image),
        }

        element = etree.Element(etree.QName(namespace_uri, "bullet"), attrib=attribs)

        q_name = etree.QName(namespace_uri, "paraHead")
        element.append(self.para_head.to_xml(q_name))

        return element
