from typing import Type

from DataType import DataType
from ..Statements.Definition import Definition

"""
class HeaderDataType(DataType):
    def __init__(self, reference, *args, **kwargs):
        if kwargs:
            for arg, kwarg in zip(args, kwargs):
                {}
            super().__init__(header)
"""


class ARRAY(DataType):
    def __init__(self, *args: Definition):
        if len(args) == 0:
            raise SyntaxError("Empty LIS header.")
        super().__init__(ARRAY, [arg for arg in args])
