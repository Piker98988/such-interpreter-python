"""Integer type in such."""
from .DataType import DataType


class INTEGER(DataType):
    def __init__(self, value: int):
        super().__init__(INTEGER, self._tryToParseValue(value))

    def _tryToParseValue(self, value: int):
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"INT type must be an integer: {value}")

    @classmethod
    def __repr__(cls):
        return f"INT"