from pydantic import BaseModel, Field


class RelSz(BaseModel):
    hangul: int = Field(default=100)
    latin: int = Field(default=100)
    hanja: int = Field(default=100)
    japanese: int = Field(default=100)
    other: int = Field(default=100)
    symbol: int = Field(default=100)
    user: int = Field(default=100)