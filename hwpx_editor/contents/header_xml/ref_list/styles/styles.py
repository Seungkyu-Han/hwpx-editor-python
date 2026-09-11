from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.styles.style import Style


class Styles(BaseModel):
    styles: list[Style] = Field(
        default_factory=lambda: [
            Style(id=0, type="PARA", name="바탕글", eng_name="Normal", para_pr_id_ref=0, char_pr_id_ref=0,
                  next_style_id_ref=0, ),
            Style(id=1, type="PARA", name="본문", eng_name="Body", para_pr_id_ref=1, char_pr_id_ref=0,
                  next_style_id_ref=1, ),
            Style(id=2, type="PARA", name="개요 1", eng_name="Outline 1", para_pr_id_ref=2, char_pr_id_ref=0,
                  next_style_id_ref=2, ),
            Style(id=3, type="PARA", name="개요 2", eng_name="Outline 2", para_pr_id_ref=3, char_pr_id_ref=0,
                  next_style_id_ref=3, ),
            Style(id=4, type="PARA", name="개요 3", eng_name="Outline 3", para_pr_id_ref=4, char_pr_id_ref=0,
                  next_style_id_ref=4, ),
            Style(id=5, type="PARA", name="개요 4", eng_name="Outline 4", para_pr_id_ref=5, char_pr_id_ref=0,
                  next_style_id_ref=5, ),
            Style(id=6, type="PARA", name="개요 5", eng_name="Outline 5", para_pr_id_ref=6, char_pr_id_ref=0,
                  next_style_id_ref=6, ),
            Style(id=7, type="PARA", name="개요 6", eng_name="Outline 6", para_pr_id_ref=7, char_pr_id_ref=0,
                  next_style_id_ref=7, ),
            Style(id=8, type="PARA", name="개요 7", eng_name="Outline 7", para_pr_id_ref=8, char_pr_id_ref=0,
                  next_style_id_ref=8, ),
            Style(id=9, type="PARA", name="개요 8", eng_name="Outline 8", para_pr_id_ref=18, char_pr_id_ref=0,
                  next_style_id_ref=9, ),
            Style(id=10, type="PARA", name="개요 9", eng_name="Outline 9", para_pr_id_ref=16, char_pr_id_ref=0,
                  next_style_id_ref=10, ),
            Style(id=11, type="PARA", name="개요 10", eng_name="Outline 10", para_pr_id_ref=17, char_pr_id_ref=0,
                  next_style_id_ref=11, ),
            Style(id=12, type="CHAR", name="쪽 번호", eng_name="Page Number", para_pr_id_ref=0, char_pr_id_ref=0,
                  next_style_id_ref=0, ),
            Style(id=13, type="PARA", name="머리말", eng_name="Header", para_pr_id_ref=9, char_pr_id_ref=1,
                  next_style_id_ref=13, ),
            Style(id=14, type="PARA", name="각주", eng_name="Footnote", para_pr_id_ref=10, char_pr_id_ref=1,
                  next_style_id_ref=14, ),
            Style(id=15, type="PARA", name="미주", eng_name="Endnote", para_pr_id_ref=10, char_pr_id_ref=1,
                  next_style_id_ref=15, ),
            Style(id=16, type="PARA", name="메모", eng_name="Memo", para_pr_id_ref=11, char_pr_id_ref=2,
                  next_style_id_ref=16, ),
            Style(id=17, type="PARA", name="차례 제목", eng_name="TOC Heading", para_pr_id_ref=12, char_pr_id_ref=3,
                  next_style_id_ref=17, ),
            Style(id=18, type="PARA", name="차례 1", eng_name="TOC 1", para_pr_id_ref=13, char_pr_id_ref=4,
                  next_style_id_ref=18, ),
            Style(id=19, type="PARA", name="차례 2", eng_name="TOC 2", para_pr_id_ref=14, char_pr_id_ref=4,
                  next_style_id_ref=19, ),
            Style(id=20, type="PARA", name="차례 3", eng_name="TOC 3", para_pr_id_ref=15, char_pr_id_ref=4,
                  next_style_id_ref=20, ),
            Style(id=21, type="PARA", name="캡션", eng_name="Caption", para_pr_id_ref=19, char_pr_id_ref=0,
                  next_style_id_ref=21, ),
        ],
    )

    def to_xml(self, namespace_uri: str) -> Any:
        """주어진 네임스페이스에 이 모델과 하위 XML 요소를 생성합니다."""
        attribs: dict[str, str] = {
            "itemCnt": str(len(self.styles)),
        }

        element = etree.Element(etree.QName(namespace_uri, "styles"), attrib=attribs)

        q_name = etree.QName(namespace_uri, "style")
        for item in self.styles:
            element.append(item.to_xml(q_name))

        return element
