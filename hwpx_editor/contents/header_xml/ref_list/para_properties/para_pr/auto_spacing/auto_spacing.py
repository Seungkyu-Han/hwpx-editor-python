from pydantic import BaseModel, Field


class AutoSpacing(BaseModel):
    e_asian_eng: int = Field(
        default=0,
        description="""
        한글과 영어 간격을 자동 조절 여부
        """
    )

    e_asian_num: int = Field(
        default=0,
        description="""
        한글과 숫자 간격을 자동 조절 여부
        """
    )