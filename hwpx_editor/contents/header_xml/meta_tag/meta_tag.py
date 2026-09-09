from pydantic import BaseModel, Field


class Meta_tag(BaseModel):
    text: str = Field(
        default="{}"
    )