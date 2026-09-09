from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.trackchange_config.config_item_set.config_item import ConfigItem


class ConfigItemSet(BaseModel):

    name: str = Field(
        default="TrackChangePasswordInfo"
    )

    config_items: list[ConfigItem] = Field(
        default_factory=lambda: [
            ConfigItem(),
        ]
    )