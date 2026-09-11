from typing import Any, Literal
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field


class BreakSetting(BaseModel):
    break_latin_word: Literal["KEEP_WORD", "BREAK_WORD"] = Field(default="KEEP_WORD", description="라틴 문자의 나눔 단위")
    break_not_latin_word: Literal["KEEP_WORD", "BREAK_WORD"] = Field(default="KEEP_WORD", description="라틴 문자 이외의 문자 줄나눔 단위")
    widow_orphan: int = Field(default=0, description="외톨이줄 보호 여부")
    keep_with_next: int = Field(default=0, description="다음 문단과 함께 여부")
    keep_lines: int = Field(default=0, description="문단 보호 여부")
    page_break_before: int = Field(default=0, description="문단 앞에서 항상 쪽 나눔 여부")
    line_wrap: Literal["BREAK"] = Field(default="WRAP_NONE", description="한 줄로 입력 사용 시의 형식")

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "breakLatinWord": str(self.break_latin_word),
            "breakNonLatinWord": str(self.break_not_latin_word),
            "widowOrphan": str(self.widow_orphan),
            "keepWithNext": str(self.keep_with_next),
            "keepLines": str(self.keep_lines),
            "pageBreakBefore": str(self.page_break_before),
            "lineWrap": str(self.line_wrap),
        }

        element = etree.Element(q_name, attrib=attribs)

        return element
