from typing import Type, override

from classes.Statements.Statement import Statement
from classes.Types.Boolean import BOOLEAN
from classes.Types.String import STRING
from classes.Types.Array import ARRAY
from classes.Types.Keymap import KEYMAP
from classes.Types.DataType import DataType


class Header(Statement):
    def __init__(self, datatype: Type[DataType], subtypes: tuple[Type[DataType], ...], name: str):
        if datatype is ARRAY or datatype is KEYMAP:
            ...
        else:
            raise TypeError("A header can only be of type VECH or RELH")

        self.subtypes = subtypes
        if type(datatype) is ARRAY:
            super().__init__(datatype, name, ARRAY)
        else:
            super().__init__(datatype, name, KEYMAP)


    @override
    def __str__(self):
        subtype_array = "{" + f"{self.subtypes[0]}" + "".join(["/" + f"{n}" for n in self.subtypes[1:]]) + "}"
        return f"{self.type}{subtype_array} {self.reference} [{self.child}]"



if __name__ == '__main__':
    header = Header(KEYMAP, (BOOLEAN, STRING), "a::b::c")
    print(header.type)