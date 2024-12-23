"""String type in such."""
from classes.Types.DataType import DataType


class STRING(DataType):
    def __init__(self, value: str):
        super().__init__(STRING, self._tryToParseValue(value))

    def _tryToParseValue(self, value):
        return value