from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.tab_properties.tab_pr import TabPr


class TabProperties(BaseModel):

    item_cnt: int = Field(default=3)

    tab_prs: list[TabPr] = Field(
        default_factory=lambda: [
            TabPr(id = 0, auto_tab_left = 0, auto_tab_right = 0),
            TabPr(id = 1, auto_tab_left = 1, auto_tab_right = 0),
            TabPr(id = 2, auto_tab_left = 0, auto_tab_right = 1),
        ]
    )

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "itemCnt": str(self.item_cnt),
        }

        element = etree.Element(etree.QName(namespace_uri, "tabProperties"), attrib=attribs)

        for item in self.tab_prs:
            element.append(item.to_xml(namespace_uri))

        return element
