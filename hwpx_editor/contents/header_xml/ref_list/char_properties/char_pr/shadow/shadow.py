from typing import Literal

from pydantic import BaseModel, Field


class Shadow(BaseModel):
    type: Literal["NONE", "DROP", "CONTINUOUS"] = Field(default="NONE")
    color: str = Field(default="#C0C0C0")
    offset_x: int = Field(default=10)
    offset_y: int = Field(default=10)