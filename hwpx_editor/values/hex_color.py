from typing import Annotated

from pydantic import StringConstraints

HexColor = Annotated[
    str,
    StringConstraints(strict=True, min_length=7, max_length=7, pattern=r"^#[0-9A-Fa-f]{6}$"),
]
"""A six-digit RGB hexadecimal color, including the leading #."""
