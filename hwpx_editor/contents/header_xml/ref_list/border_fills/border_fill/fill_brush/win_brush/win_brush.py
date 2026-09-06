from pydantic import BaseModel, Field


class WinBrush(BaseModel):
    face_color: str = Field(default="none")
    hatch_color: str = Field(default="#999999")
    alpha: float = Field(default=0, description="투명도")