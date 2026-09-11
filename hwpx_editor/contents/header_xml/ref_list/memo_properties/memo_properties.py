from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.memo_properties.memo_pr import MemoPr


class MemoProperties(BaseModel):
    item_cnt: int = Field(default=0)

    memo_properties: list[MemoPr] = Field(default_factory=lambda: [])

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "itemCnt": str(self.item_cnt),
        }

        element = etree.Element(etree.QName(namespace_uri, "memoProperties"), attrib=attribs)

        q_name = etree.QName(namespace_uri, "memoPr")
        for item in self.memo_properties:
            element.append(item.to_xml(q_name))

        return element
