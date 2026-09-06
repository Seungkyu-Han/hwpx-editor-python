from pydantic import BaseModel, Field

from hwpx_editor.contents.header_xml.ref_list.bullets.bullet import Bullet


class Bullets(BaseModel):

    item_cnt: int = Field(default=1)

    bullets: list[Bullet] = Field(
        default_factory=lambda: [Bullet(
            id=1,
        )],
    )