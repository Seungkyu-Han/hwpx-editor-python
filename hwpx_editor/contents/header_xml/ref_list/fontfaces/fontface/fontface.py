from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.fontfaces.fontface.font import Font
from hwpx_editor.enums import Lang


class Fontface(BaseModel):
    lang: Lang = Field(description="")
    font_cnt: int = Field(default=1, description="fontCnt")
    font: list[Font] = Field(
        default_factory=lambda: [Font()],
    )

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "lang": str(self.lang),
            "fontCnt": str(self.font_cnt),
        }

        element = etree.Element(etree.QName(namespace_uri, "fontface"), attrib=attribs)

        for item in self.font:
            element.append(item.to_xml(namespace_uri))

        return element
