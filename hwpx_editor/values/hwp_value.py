from typing import Literal

from pydantic import BaseModel, Field


class HWPValue(BaseModel):
    value: int = Field(default=0, description="실제 값")
    unit: Literal["CHAR", "HWPUNIT"] = Field(default="CHAR", description="값의 단위")
