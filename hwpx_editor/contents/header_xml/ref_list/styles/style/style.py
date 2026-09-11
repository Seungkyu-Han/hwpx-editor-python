from typing import Any, Literal
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field


class Style(BaseModel):
    id: int = Field(
        ge=0,
    )

    type: Literal["PARA", "CHAR"] = Field()

    name: str = Field()

    eng_name: str = Field()

    para_pr_id_ref: int = Field()

    char_pr_id_ref: int = Field()

    next_style_id_ref: int = Field()

    lang_id: int = Field(default=1042)

    lock_form: int = Field(default=0)

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "id": str(self.id),
            "type": str(self.type),
            "name": str(self.name),
            "engName": str(self.eng_name),
            "paraPrIDRef": str(self.para_pr_id_ref),
            "charPrIDRef": str(self.char_pr_id_ref),
            "nextStyleIDRef": str(self.next_style_id_ref),
            "langID": str(self.lang_id),
            "lockForm": str(self.lock_form),
        }

        element = etree.Element(q_name, attrib=attribs)

        return element
