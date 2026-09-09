from pydantic import BaseModel, Field


class ForbiddenWord(BaseModel):

    text: str = Field(
        description="""
        금칙 문자
        요소의 값으로 문자열을 가짐.
        """
    )