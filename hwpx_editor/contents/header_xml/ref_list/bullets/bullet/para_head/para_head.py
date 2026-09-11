from typing import Any, Literal, Optional
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.enums import NumberType1


class ParaHead(BaseModel):
    level: int = Field(ge=0)
    align: Literal["LEFT", "RIGHT", "CENTER"] = Field(default="LEFT")
    use_inst_width: int = Field(default=0)
    auto_indent: int = Field(default=1)
    width_adjust: int = Field(default=0)
    text_offset_type: Literal["PERCENT", "HWPUNIT"] = Field(default="PERCENT")
    text_offset: int = Field(default=50)
    num_format: NumberType1 = Field(default=NumberType1.DIGIT)
    char_pr_id_ref: int = Field()
    checkable: int = Field()
    text: Optional[str] = Field(default=None)

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "level": str(self.level),
            "align": str(self.align),
            "useInstWidth": str(self.use_inst_width),
            "autoIndent": str(self.auto_indent),
            "widthAdjust": str(self.width_adjust),
            "textOffsetType": str(self.text_offset_type),
            "textOffset": str(self.text_offset),
            "numFormat": str(self.num_format),
            "charPrIDRef": str(self.char_pr_id_ref),
            "checkable": str(self.checkable),
        }

        element = etree.Element(q_name, attrib=attribs)

        if self.text is not None:
            element.text = self.text

        return element
