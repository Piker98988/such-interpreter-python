"""Base class for any statement in such."""
from typing import Type

from utils.Types.DataType import DataType


class Statement(object):
    """Base class for any statement in such."""
    def __init__(self, datatype: Type[DataType], reference: str, child: DataType):
        self.datatype = datatype
        """Which type is the child of this statement"""
        self.reference = reference
        """What is the reference of the child of this statement"""
        self.child = child
        """The child of this statement"""