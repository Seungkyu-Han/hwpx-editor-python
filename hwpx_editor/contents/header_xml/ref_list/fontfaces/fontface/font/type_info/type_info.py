from typing import Any, Optional
from lxml.etree import QName

from lxml import etree
from pydantic import BaseModel, Field



class TypeInfo(BaseModel):
    family_type: Optional[str] = Field(default="FCAT_UNKNOWN", description="familyType")
    serif_style: Optional[str] = Field(default=None, description="serifStyle")
    weight: int = Field(default=0, description="weight")
    proportion: int = Field(default=0, description="proportion")
    contrast: str = Field(default=0, description="contrast")
    stroke_variation: int = Field(default=0, description="strokeVariation")
    arm_style: int = Field(default=0, description="armStyle")
    letterform: int = Field(default=0, description="letterform")
    midline: int = Field(default=252, description="midline")
    x_height: int = Field(default=255, description="xHeight")

    def to_xml(self, q_name: QName) -> Any:
        """이 모델을 주어진 태그의 XML 요소로 변환합니다."""
        attribs: dict[str, str] = {
            "weight": str(self.weight),
            "proportion": str(self.proportion),
            "contrast": str(self.contrast),
            "strokeVariation": str(self.stroke_variation),
            "armStyle": str(self.arm_style),
            "letterform": str(self.letterform),
            "midline": str(self.midline),
            "xHeight": str(self.x_height),
        }

        if self.family_type is not None:
            attribs["familyType"] = str(self.family_type)

        if self.serif_style is not None:
            attribs["serifStyle"] = str(self.serif_style)

        element = etree.Element(q_name, attrib=attribs)

        return element
