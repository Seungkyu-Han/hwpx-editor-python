from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.trackchange_config.config_item_set import ConfigItemSet


class TrackchangeConfig(BaseModel):

    flags: int = Field(default=56)

    config_item_sets: list[ConfigItemSet] = Field(
        default_factory=lambda: [
            ConfigItemSet()
        ]
    )