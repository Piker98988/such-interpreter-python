from typing import Type, override

from Statement import Statement
from classes.Types.Boolean import BOOLEAN
from ..Types.Array import ARRAY
from ..Types.Keymap import KEYMAP
from ..Types.DataType import DataType


class Header(Statement):
    def __init__(self, datatype: Type[DataType], subtypes: tuple[DataType], name):
        if type(datatype) is not ARRAY or type(subtypes) is not KEYMAP:
            raise TypeError("A header can only be of type LIS or KYV")
        self.subtypes = subtypes
        if type(datatype) is ARRAY:
            super().__init__(datatype, name, ARRAY)
        else:
            super().__init__(datatype, name, KEYMAP)


    @override
    def __str__(self):
        subtype_array = "{" + f"{self.subtypes[0]}" + "".join(["/" + f"{n}" for n in self.subtypes[1:]]) + "}"
        return f"{self.type}{subtype_array} {self.reference} [{self.child}]"
    """   

    def __str__(self) -> str:
        return f"{self.main_type}{{{self.datatypes[0]+["/" + n for n in self.datatypes[1:]]}}} {self.name} --- [{self.contents}]))"
    """


if __name__ == '__main__':
    header = Header(BOOLEAN, "asd", ())
    print(header.type)