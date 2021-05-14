from enum import Enum, auto


class BodyPart(Enum):
    NOTHING = auto()
    HEAD = auto()
    BELLY = auto()
    LEGS = auto()

    @classmethod
    def min_value(cls):
        return cls.NOTHING.value

    @classmethod
    def max_value(cls):
        return cls.LEGS.value

    @classmethod
    def has_item(cls, name: str):
        return name in cls._member_names_
