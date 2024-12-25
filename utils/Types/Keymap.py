"""Relational Header type in such."""
from utils.Statements.Definition import Definition
from utils.Statements.Statement import Statement
from utils.Types.DataType import DataType


class KEYMAP(DataType):
    """
    A relational header, which will have as children any amount of definitions or headers.
    """
    def __init__(self, subtypes):
        self.subtypes = subtypes
        super().__init__(KEYMAP, [])

    def _add_child(self, child: Statement):
        if child.datatype in self.subtypes:
            self.value.append(child)
        else:
            raise TypeError(f"Incorrect type for child: {child}, child type: {child.datatype} not in containing types of header: {self.subtypes} at header: {self.__str__()}")
