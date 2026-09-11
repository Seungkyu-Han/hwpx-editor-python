from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.compatible_document.layout_compatibility import LayoutCompatibility


class CompatibleDocument(BaseModel):

    target_program: str = Field(
        default="HWP201X",
    )

    layout_compatibility: LayoutCompatibility = Field(
        default_factory=lambda: LayoutCompatibility(),
    )

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "targetProgram": str(self.target_program),
        }

        element = etree.Element(etree.QName(namespace_uri, "compatibleDocument"), attrib=attribs)

        q_name = etree.QName(namespace_uri, "layoutCompatibility")
        element.append(self.layout_compatibility.to_xml(q_name))

        return element
