"""Null type in such."""
from DataType import DataType


class NULL(DataType):
    def __init__(self):
        super().__init__("NU?", None)
