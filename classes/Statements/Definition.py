"""Definition of a TYPE NAME = VALUE; statement in such."""
from typing import Type

from classes.Types.DataType import DataType
from classes.Types.NullType import NULL


class Definition(object):
    def __init__(self, datatype: Type[DataType], name, value: DataType):
        if not issubclass(datatype, DataType):
            raise TypeError(f"Invalid type: {datatype}")

        self.datatype = datatype
        self.name = name
        if datatype is not NULL:
            self.value = datatype(value)
        else:
            self.value = None

    def __str__(self) -> str:
        return f"definition: {self.datatype.__name__} {self.name} = {self.value}"

    @classmethod
    def __repr__(cls) -> str:
        return f"class: {cls.__name__}"

