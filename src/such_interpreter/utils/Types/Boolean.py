"""Boolean type in such."""
from .DataType import DataType


class BOOLEAN(DataType):
    def __init__(self, value: bool):
        super().__init__(BOOLEAN, self._tryToParseValue(value))


    def _tryToParseValue(self, value) -> bool:
        if value == "true" or value:
            return True
        elif value == "false" or not value:
            return False

        raise TypeError("BOO type must be true or false")

    @classmethod
    def __repr__(cls):
        return f"BOO"