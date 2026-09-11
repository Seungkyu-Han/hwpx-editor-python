from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.begin_num import BeginNum
from hwpx_editor.contents.header_xml.compatible_document import CompatibleDocument
from hwpx_editor.contents.header_xml.doc_option import DocOption
from hwpx_editor.contents.header_xml.forbidden_word_list import ForbiddenWordList
from hwpx_editor.contents.header_xml.meta_tag import MetaTag
from hwpx_editor.contents.header_xml.ref_list import RefList
from hwpx_editor.contents.header_xml.trackchange_config import TrackchangeConfig
from hwpx_editor.namespaces import namespaces


class HeaderXml(BaseModel):
    version: str = Field(default="1.5")
    sec_cnt: int = Field(default=1, ge=1)
    begin_num: BeginNum = Field(default_factory=BeginNum)
    ref_list: RefList = Field(default_factory=RefList)
    forbidden_word_list: ForbiddenWordList = Field(default_factory=ForbiddenWordList)
    compatible_document: CompatibleDocument = Field(default_factory=CompatibleDocument)
    doc_option: DocOption = Field(default_factory=DocOption)
    meta_tag: MetaTag = Field(default_factory=MetaTag)
    trackchange_config: TrackchangeConfig = Field(default_factory=TrackchangeConfig)

    def to_xml(self) -> etree._Element:
        """모델의 현재 값으로 header.xml 루트 요소를 생성합니다."""
        hh = namespaces["hh"]
        root = etree.Element(
            etree.QName(hh, "head"), nsmap=namespaces,
            attrib={"version": self.version, "secCnt": str(self.sec_cnt)},
        )
        root.append(self.begin_num.to_xml(etree.QName(hh, "beginNum")))
        root.append(self.ref_list.to_xml(hh, namespaces["hc"]))
        root.append(self.forbidden_word_list.to_xml(hh))
        root.append(self.compatible_document.to_xml(hh))
        root.append(self.doc_option.to_xml(hh))
        root.append(self.meta_tag.to_xml(etree.QName(hh, "metaTag")))
        root.append(self.trackchange_config.to_xml(hh))
        return root

    @property
    def xml(self) -> str:
        return etree.tostring(
            self.to_xml(), encoding="UTF-8", xml_declaration=True,
            standalone=True, pretty_print=True,
        ).decode("utf-8")
