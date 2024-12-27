"""String type in such."""
from .DataType import DataType


class STRING(DataType):
    def __init__(self, value: str):
        super().__init__(STRING, self._tryToParseValue(value))

    def _tryToParseValue(self, value):
        return value.removeprefix("\"").removeprefix("'").removesuffix("\"").removesuffix("'")

    @classmethod
    def __repr__(cls):
        return f"STR"