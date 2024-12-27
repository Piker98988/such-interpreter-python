"""Relational Header type in such."""
from ..Statements.Statement import Statement
from .DataType import DataType


class KEYMAP(DataType):
    """
    A relational header, which will have as children any amount of definitions or headers.
    """
    def __init__(self, subtypes):
        self.subtypes = subtypes
        super().__init__(KEYMAP, [])
        self.value: list

    def _add_child(self, child: Statement):
        if child.datatype in self.subtypes:
            self.value.append(child)
        else:
            raise TypeError(f"Incorrect type for child: {child}, child type: {child.datatype} not in containing types of header: {self.subtypes} at header: {self.__str__()}")


    def __str__(self) -> str:
        return f"KEYMAP({[v.__str__() for v in self.value if self.value is not None]})"

    @classmethod
    def __repr__(cls):
        return f"RELH"