"""Integer type in such."""
from DataType import DataType


class INTEGER(DataType):
    def __init__(self, value: int):
        if type(value) is not int:
            raise ValueError("INT type must be an integer")

        super().__init__(INTEGER, value)
