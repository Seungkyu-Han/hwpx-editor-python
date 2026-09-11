from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.doc_option.linkinfo import LinkInfo


class DocOption(BaseModel):

    linkinfo: LinkInfo = Field(
        default_factory=lambda: LinkInfo(),
    )

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
        }

        element = etree.Element(etree.QName(namespace_uri, "docOption"), attrib=attribs)

        q_name = etree.QName(namespace_uri, "linkinfo")
        element.append(self.linkinfo.to_xml(q_name))

        return element
