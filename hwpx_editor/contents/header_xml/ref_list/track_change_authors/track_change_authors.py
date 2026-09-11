from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.track_change_authors.track_change_author import TrackChangeAuthor


class TrackChangeAuthors(BaseModel):
    item_cnt: int = Field(default=1)

    track_change_authors: list[TrackChangeAuthor] = Field(
        default_factory=lambda: [
            TrackChangeAuthor(id=1, name="hancom", mark=1, color=None)
        ]
    )

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "itemCnt": str(self.item_cnt),
        }

        element = etree.Element(etree.QName(namespace_uri, "trackChangeAuthors"), attrib=attribs)

        q_name = etree.QName(namespace_uri, "trackChangeAuthor")
        for item in self.track_change_authors:
            element.append(item.to_xml(q_name))

        return element
