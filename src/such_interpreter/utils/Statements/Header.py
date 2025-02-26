from typing import Type, override

from .Definition import Definition
from .Statement import Statement
from ..Types.Array import ARRAY
from ..Types.DataType import DataType
from ..Types.Keymap import KEYMAP


class Header(Statement):
    def __init__(self, datatype: Type[DataType], subtypes: tuple[Type[DataType], ...], name: str):
        if datatype is not ARRAY and datatype is not KEYMAP:
            raise TypeError("A header can only be of type VECH or RELH")

        self.subtypes = tuple(subtypes)
        self.real_reference: str = name.split("::")[-1]
        self.nesting: int = name.split("::").__len__() - 1

        if datatype is ARRAY:
            super().__init__(datatype, name, [])
            self.child: ARRAY | KEYMAP = ARRAY(self.subtypes)
        else:
            super().__init__(datatype, name, [])
            self.child: ARRAY | KEYMAP = KEYMAP(self.subtypes)

    @override
    def __str__(self):
        subtype_array = ("{" + f"{self.subtypes[0].__repr__()}" + "".join(["/" + f"{n.__repr__()}" for n in self.subtypes[1:]]) + "}")
        return f"{self.datatype.__repr__()}{{{subtype_array}}} {self.reference} = [ {self.child.__str__()} ]"

    def add_child(self, child: Statement):
        if isinstance(child, Definition):
            self._add_definition_child(child)

        if isinstance(child, Header):
            self._add_header_child(child)

    def _add_definition_child(self, child: Statement):
        self.child._add_child(child)

    def _add_header_child(self, child: Statement):
        self.child._add_child(child)
