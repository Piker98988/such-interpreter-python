"""Definition of a TYPE NAME = VALUE; statement in such."""
from typing import Type

from utils.Statements.Statement import Statement
from utils.Types.DataType import DataType
from utils.Types.NullType import NULL


class Definition(Statement):
    def __init__(self, datatype: Type[DataType], name, value: DataType):
        if not issubclass(datatype, DataType):
            raise TypeError(f"Invalid type: {datatype}")

        if datatype is not NULL:
            super().__init__(datatype, name, datatype(value))
        else:
            # ? Null is a special case.
            # ? Null is null, its value can't be different from Null, so parameters will be evaluated and then discarded.

            super().__init__(datatype, name, NULL(value))

    def __str__(self) -> str:
        return f"definition: {self.datatype.__name__} {self.reference} = {self.child}"

    @classmethod
    def __repr__(cls) -> str:
        return f"class: {cls.__name__}"

