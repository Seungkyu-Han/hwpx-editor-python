from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.numberings.numbering import Numbering


class Numberings(BaseModel):
    numberings: list[Numbering] = Field(
        default_factory=lambda: [Numbering()],
    )

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "itemCnt": str(len(self.numberings)),
        }

        element = etree.Element(etree.QName(namespace_uri, "numberings"), attrib=attribs)

        for item in self.numberings:
            element.append(item.to_xml(namespace_uri))

        return element
