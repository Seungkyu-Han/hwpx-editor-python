from pydantic import BaseModel, Field


class LinkInfo(BaseModel):
    path: str = Field(default="")
    page_inherit: int = Field(default=0)
    footnote_inherit: int = Field(default=0)
