from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.numberings.numbering.para_head import ParaHead
from hwpx_editor.enums import NumberType1


class Numbering(BaseModel):
    id: int = Field(default=1)
    start: int = Field(default=0)

    para_heads: list[ParaHead] = Field(
        default_factory=lambda: [
            ParaHead(
                start=1,
                level=1,
                num_format=NumberType1.DIGIT,
                char_pr_id_ref=4294967295,
                checkable=0,
                text="^1.",
            ),
            ParaHead(
                start=1,
                level=2,
                num_format=NumberType1.HANGUL_SYLLABLE,
                char_pr_id_ref=4294967295,
                checkable=0,
                text="^2.",
            ),
            ParaHead(
                start=1,
                level=3,
                num_format=NumberType1.DIGIT,
                char_pr_id_ref=4294967295,
                checkable=0,
                text="^3)",
            ),
            ParaHead(
                start=1,
                level=4,
                align="LEFT",
                num_format=NumberType1.HANGUL_SYLLABLE,
                char_pr_id_ref=4294967295,
                checkable=0,
                text="^4)",
            ),
            ParaHead(
                start=1,
                level=5,
                num_format=NumberType1.DIGIT,
                char_pr_id_ref=4294967295,
                checkable=0,
                text="(^5)",
            ),
            ParaHead(
                start=1,
                level=6,
                num_format=NumberType1.HANGUL_SYLLABLE,
                char_pr_id_ref=4294967295,
                checkable=0,
                text="(^6)",
            ),
            ParaHead(
                start=1,
                level=7,
                num_format=NumberType1.CIRCLED_DIGIT,
                char_pr_id_ref=4294967295,
                checkable=1,
                text="^7",
            ),
            ParaHead(
                start=1,
                level=8,
                num_format=NumberType1.CIRCLED_HANGUL_SYLLABLE,
                char_pr_id_ref=4294967295,
                checkable=1,
                text="^8",
            ),
            ParaHead(
                start=1,
                level=9,
                num_format=NumberType1.HANGUL_JAMO,
                char_pr_id_ref=4294967295,
                checkable=0,
            ),
            ParaHead(
                start=1,
                level=10,
                num_format=NumberType1.ROMAN_SMALL,
                char_pr_id_ref=4294967295,
                checkable=1,
            ),
        ]
    )