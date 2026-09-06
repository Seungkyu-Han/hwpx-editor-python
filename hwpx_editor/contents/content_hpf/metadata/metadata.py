from datetime import datetime, timezone
from typing import Any

from lxml import etree
from pydantic import BaseModel, Field

from hwpx_editor.contents.content_hpf.metadata.meta import Meta


def _get_date() -> str:
    now = datetime.now()

    days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    day_str = days[now.weekday()]

    am_pm = "오전" if now.hour < 12 else "오후"
    hour_12 = now.hour % 12
    if hour_12 == 0:
        hour_12 = 12

    return f"{now.year}년 {now.month}월 {now.day}일 {day_str} {am_pm} {hour_12}:{now.minute:02d}:{now.second:02d}"


class Metadata(BaseModel):
    title: str = Field(default="제목없음", description="Title of the content")
    language: str = Field(default="ko", description="Language of the content")

    created_date: Meta = Field(
        default_factory=lambda: Meta(
            name="CreatedDate",
            text=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        )
    )
    modified_date: Meta = Field(
        default_factory=lambda: Meta(
            name="ModifiedDate",
            text=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        )
    )
    date: Meta = Field(
        default_factory=lambda: Meta(name="date", text=_get_date()),
        description="date",
    )

    def to_xml(self, opf_uri: str) -> Any:

        metadata_element = etree.Element(etree.QName(opf_uri, "metadata"))

        title_element = etree.SubElement(metadata_element, etree.QName(opf_uri, "title"))
        title_element.text = self.title

        lang_element = etree.SubElement(metadata_element, etree.QName(opf_uri, "language"))
        lang_element.text = self.language

        q_name = etree.QName(opf_uri, "meta")

        for meta in (self.created_date, self.modified_date, self.date):
            meta_element = meta.to_xml(q_name)
            metadata_element.append(meta_element)

        return metadata_element