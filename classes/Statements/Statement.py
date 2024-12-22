"""Base class for any statement in such."""
from typing import Type

from ..Types.DataType import DataType


class Statement(object):
    def __init__(self, type: Type[DataType], reference: str, child: Type[DataType]):
        self.type = type
        self.reference = reference
        self.child = child