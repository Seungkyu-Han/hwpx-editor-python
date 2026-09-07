from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.para_properties.para_pr.align import Align
from hwpx_editor.contents.header_xml.ref_list.para_properties.para_pr.break_setting import BreakSetting
from hwpx_editor.contents.header_xml.ref_list.para_properties.para_pr.heading import Heading
from hwpx_editor.contents.header_xml.ref_list.para_properties.para_pr.line_spacing import LineSpacing
from hwpx_editor.contents.header_xml.ref_list.para_properties.para_pr.margin import Margin
from hwpx_editor.contents.header_xml.ref_list.para_properties.para_pr.para_pr import ParaPr
from hwpx_editor.values import HWPValue


class ParaProperties(BaseModel):
    item_cnt: int = Field(default=20)

    para_prs: list[ParaPr] = Field(
        default_factory= lambda: [
            ParaPr(
                id=0,
                align=Align(
                    horizontal="JUSTIFY",
                    vertical="BASELINE",
                ),
            ),
            ParaPr(
                id=1,
                align=Align(
                    horizontal="JUSTIFY",
                    vertical="BASELINE",
                ),
                margin=Margin(left=HWPValue(value=1500)),
            ),
            ParaPr(
                id=2,
                tab_pr_id_ref=1,
                condense=20,
                heading=Heading(type="OUTLINE"),
                align=Align(
                    horizontal="JUSTIFY",
                    vertical="BASELINE",
                ),
                margin=Margin(left=HWPValue(value=1000)),
            ),
            ParaPr(
                id=3,
                tab_pr_id_ref=1,
                condense=20,
                heading=Heading(type="OUTLINE", level=1),
                align=Align(
                    horizontal="JUSTIFY",
                    vertical="BASELINE",
                ),
                margin=Margin(left=HWPValue(value=2000)),
            ),
            ParaPr(
                id=4,
                tab_pr_id_ref=1,
                condense=20,
                heading=Heading(type="OUTLINE", level=2),
                align=Align(
                    horizontal="JUSTIFY",
                    vertical="BASELINE",
                ),
                margin=Margin(left=HWPValue(value=3000)),
            ),
            ParaPr(
                id=5,
                tab_pr_id_ref=1,
                condense=20,
                heading=Heading(type="OUTLINE", level=3),
                align=Align(
                    horizontal="JUSTIFY",
                    vertical="BASELINE",
                ),
                margin=Margin(left=HWPValue(value=4000)),
            ),
            ParaPr(
                id=6,
                tab_pr_id_ref=1,
                condense=20,
                heading=Heading(type="OUTLINE", level=4),
                align=Align(
                    horizontal="JUSTIFY",
                    vertical="BASELINE",
                ),
                margin=Margin(left=HWPValue(value=5000)),
            ),
            ParaPr(
                id=7,
                tab_pr_id_ref=1,
                condense=20,
                heading=Heading(type="OUTLINE", level=5),
                align=Align(
                    horizontal="JUSTIFY",
                    vertical="BASELINE",
                ),
                margin=Margin(left=HWPValue(value=6000)),
            ),
            ParaPr(
                id=8,
                tab_pr_id_ref=1,
                condense=20,
                heading=Heading(type="OUTLINE", level=6),
                align=Align(
                    horizontal="JUSTIFY",
                    vertical="BASELINE",
                ),
                margin=Margin(left=HWPValue(value=7000)),
            ),
            ParaPr(
                id=9,
                break_setting=BreakSetting(break_not_latin_word="BREAK_WORD"),
                align=Align(
                    horizontal="JUSTIFY",
                    vertical="BASELINE",
                ),
                line_spacing=LineSpacing(value=150),
            ),
            ParaPr(
                id=10,
                margin=Margin(intent=HWPValue(value=-1310)),
                align=Align(
                    horizontal="JUSTIFY",
                    vertical="BASELINE",
                ),
                line_spacing=LineSpacing(value=130),
            ),
            ParaPr(
                id=11,
                break_setting=BreakSetting(break_not_latin_word="BREAK_WORD"),
                align=Align(
                    vertical="BASELINE",
                ),
                line_spacing=LineSpacing(value=130),
            ),
            ParaPr(
                id=12,
                tab_pr_id_ref=1,
                break_setting=BreakSetting(break_not_latin_word="BREAK_WORD"),
                align=Align(
                    vertical="BASELINE",
                ),
                margin=Margin(prev=HWPValue(value=1000), next=HWPValue(value=300)),
            ),
            ParaPr(
                id=13,
                tab_pr_id_ref=2,
                break_setting=BreakSetting(break_not_latin_word="BREAK_WORD"),
                align=Align(
                    horizontal="JUSTIFY",
                    vertical="BASELINE",
                ),
                margin=Margin(next=HWPValue(value=700)),
            ),
            ParaPr(
                id=14,
                tab_pr_id_ref=2,
                break_setting=BreakSetting(break_not_latin_word="BREAK_WORD"),
                align=Align(
                    vertical="BASELINE",
                ),
                margin=Margin(left=HWPValue(value=1100), next=HWPValue(value=700)),
            ),
            ParaPr(
                id=15,
                tab_pr_id_ref=2,
                break_setting=BreakSetting(break_not_latin_word="BREAK_WORD"),
                align=Align(
                    horizontal="JUSTIFY",
                    vertical="BASELINE",
                ),
                margin=Margin(left=HWPValue(value=2200), next=HWPValue(value=700)),
            ),
            ParaPr(
                id=16,
                tab_pr_id_ref=1,
                heading=Heading(type="OUTLINE", id_ref=0, level=8),
                align=Align(
                    horizontal="JUSTIFY",
                    vertical="BASELINE",
                ),
                margin=Margin(left=HWPValue(value=9000)),
            ),
            ParaPr(
                id=17,
                tab_pr_id_ref=1,
                heading=Heading(type="OUTLINE", id_ref=0, level=9),
                align=Align(
                    horizontal="JUSTIFY",
                    vertical="BASELINE",
                ),
                margin=Margin(left=HWPValue(value=10000)),
            ),
            ParaPr(
                id=18,
                tab_pr_id_ref=1,
                heading=Heading(type="OUTLINE", id_ref=0, level=7),
                align=Align(
                    horizontal="JUSTIFY",
                    vertical="BASELINE",
                ),
                margin=Margin(left=HWPValue(value=8000)),
            ),
            ParaPr(
                id=19,
                align=Align(
                    horizontal="JUSTIFY",
                    vertical="BASELINE",
                ),
                line_spacing=LineSpacing(value=150),
                margin=Margin(left=HWPValue(value=800)),
            ),
        ]
    )