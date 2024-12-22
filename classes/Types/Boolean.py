"""Boolean type in such."""
from classes.Types.DataType import DataType


class BOOLEAN(DataType):
    def __init__(self, value: bool):
        if value:
            super().__init__("BOO", True)
        elif not value:
            super().__init__("BOO", False)
        else:
            raise TypeError("BOOLEAN type must be true or false")
