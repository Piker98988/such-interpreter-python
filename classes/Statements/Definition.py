"""Definition of a TYPE NAME = VALUE; statement in such."""
from typing import Type

from classes.Types.DataType import DataType


class Definition(object):
    def __init__(self, datatype, name, value):
        if datatype is not Type[DataType]:
            raise ValueError(f"Datatype {datatype} not supported")
        if type(value) is not Type[DataType]:
            raise TypeError(f"Value {value} is not of type {datatype}")
        self.datatype = datatype
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"{self.datatype} {self.name} = {self.value}"