from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.compatible_document.layout_compatibility import LayoutCompatibility


class CompatibleDocument(BaseModel):

    target_program: str = Field(
        default="HWP201X",
    )

    layout_compatibility: LayoutCompatibility = Field(
        default_factory=lambda: LayoutCompatibility(),
    )