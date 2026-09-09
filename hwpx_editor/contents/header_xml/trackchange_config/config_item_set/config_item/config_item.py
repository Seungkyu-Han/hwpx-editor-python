from pydantic import BaseModel, Field


class ConfigItem(BaseModel):
    name: str = Field(
        default="algorithm-name"
    )

    type: str = Field(
        default="string"
    )

    text: str = Field(
        default="SHA1"
    )