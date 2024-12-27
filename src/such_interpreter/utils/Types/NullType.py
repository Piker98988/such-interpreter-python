"""Null type in such."""
from .DataType import DataType


class NULL(DataType):
    def __init__(self, value):
        super().__init__(NULL, self._tryToParseValue(value))

    def _tryToParseValue(self, value):
        interpreted_as_null = [
            '""',
            "null",
            "none",
        ]
        if value in interpreted_as_null:
            return None

        raise ValueError(f"NU? type must be null or \"\": {value}")

    @classmethod
    def __repr__(cls):
        return f"NU?"