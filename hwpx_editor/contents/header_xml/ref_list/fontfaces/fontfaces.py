from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.fontfaces.fontface import Fontface
from hwpx_editor.enums import Lang


class FontFaces(BaseModel):
    item_cnt: int = Field(default=7, description="itemCnt")
    fontfaces: list[Fontface] = Field(
        default_factory=lambda: [
            Fontface(lang=Lang.HANGUL),
            Fontface(lang=Lang.LATIN),
            Fontface(lang=Lang.HANJA),
            Fontface(lang=Lang.JAPANESE),
            Fontface(lang=Lang.OTHER),
            Fontface(lang=Lang.SYMBOL),
            Fontface(lang=Lang.USER),
        ],
        description="fontface",
    )

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "itemCnt": str(self.item_cnt),
        }

        element = etree.Element(etree.QName(namespace_uri, "fontfaces"), attrib=attribs)

        for item in self.fontfaces:
            element.append(item.to_xml(namespace_uri))

        return element
