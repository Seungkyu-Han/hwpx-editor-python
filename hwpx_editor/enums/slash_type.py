from enum import StrEnum


class SlashType(StrEnum):
    NONE = "NONE"
    CENTER = "CENTER"
    CENTER_BELOW = "CENTER_BELOW"
    CENTER_ABOVE = "CENTER_ABOVE"
    ALL = "ALL"