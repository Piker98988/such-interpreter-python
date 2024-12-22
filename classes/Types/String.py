"""String type in such."""
from classes.Types.DataType import DataType


class STRING(DataType):
    def __init__(self, value: str):
        if type(value) is not str:
            raise TypeError("Value must be a string")
        super().__init__("STR", value)
