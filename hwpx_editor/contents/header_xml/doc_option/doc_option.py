from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.doc_option.linkinfo import LinkInfo


class DocOption(BaseModel):

    linkinfo: LinkInfo = Field(
        default_factory=lambda: LinkInfo(),
    )