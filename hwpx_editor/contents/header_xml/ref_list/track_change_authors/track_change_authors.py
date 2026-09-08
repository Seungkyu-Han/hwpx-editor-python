from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.track_change_authors.track_change_author import TrackChangeAuthor


class TrackChangeAuthors(BaseModel):
    item_cnt: int = Field(default=1)

    track_change_authors: list[TrackChangeAuthor] = Field(
        default_factory=lambda: [
            TrackChangeAuthor(id=1, name="hancom", mark=1, color=None)
        ]
    )
