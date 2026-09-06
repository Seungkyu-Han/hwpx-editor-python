from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.bullets.bullet.para_head import ParaHead


class Bullet(BaseModel):
    id: int = Field()
    char: str = Field(default="a")
    use_image: int = Field(default=0)

    para_head: ParaHead = Field(default_factory=lambda: ParaHead(level=0, char_pr_id_ref=4294967295, checkable=0))