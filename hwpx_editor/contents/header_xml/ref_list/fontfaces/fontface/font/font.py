from typing import Any, Optional

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.fontfaces.fontface.font.type_info import TypeInfo


class Font(BaseModel):
    id: int = Field(default=0)
    face: str = Field(default="맑은 고딕")
    type: str = Field(default="TTF")
    is_embedded: int = Field(default=0)
    binary_item_id_ref: Optional[int] = Field(default=None)
    type_info: TypeInfo = Field(default_factory=lambda: TypeInfo())

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "id": str(self.id),
            "face": str(self.face),
            "type": str(self.type),
            "isEmbedded": str(self.is_embedded),
        }

        if self.binary_item_id_ref is not None:
            attribs["binaryItemIDRef"] = str(self.binary_item_id_ref)

        element = etree.Element(etree.QName(namespace_uri, "font"), attrib=attribs)

        q_name = etree.QName(namespace_uri, "typeInfo")
        element.append(self.type_info.to_xml(q_name))

        return element
