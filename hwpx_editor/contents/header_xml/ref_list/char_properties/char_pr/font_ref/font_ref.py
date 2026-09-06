from pydantic import BaseModel, Field


class FontRef(BaseModel):
    hangul: int = Field(default=0)
    latin: int = Field(default=0)
    hanja: int = Field(default=0)
    japanese: int = Field(default=0)
    other: int = Field(default=0)
    symbol: int = Field(default=0)
    user: int = Field(default=0)