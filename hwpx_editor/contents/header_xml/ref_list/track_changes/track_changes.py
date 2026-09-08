from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.track_changes.track_change import TrackChange


class TrackChanges(BaseModel):

    item_cnt: int = Field(
        default=0)

    track_changes: list[TrackChange] = Field(
        default_factory=lambda: [],
    )