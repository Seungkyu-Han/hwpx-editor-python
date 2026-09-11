from typing import Any, Optional

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.tab_properties.tab_pr.tab_item import TabItem


class TabPr(BaseModel):
    id: int = Field()
    auto_tab_left: int = Field()
    auto_tab_right: int = Field()

    tab_item: Optional[TabItem] = Field(default=None)

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "id": str(self.id),
            "autoTabLeft": str(self.auto_tab_left),
            "autoTabRight": str(self.auto_tab_right),
        }

        element = etree.Element(etree.QName(namespace_uri, "tabPr"), attrib=attribs)

        if self.tab_item is not None:
            q_name = etree.QName(namespace_uri, "tabItem")
            element.append(self.tab_item.to_xml(q_name))

        return element
