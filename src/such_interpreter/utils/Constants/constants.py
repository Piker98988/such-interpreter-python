from types import NoneType
from typing import Type

from ..Types.Array import ARRAY
from ..Types.Boolean import BOOLEAN
from ..Types.DataType import DataType
from ..Types.Integer import INTEGER
from ..Types.Keymap import KEYMAP
from ..Types.NullType import NULL
from ..Types.String import STRING

htypes: dict[str, Type[DataType]] = {
    "RELH": KEYMAP,
    "VECH": ARRAY,
}
"""Relation between how the header types are written on-prem and how the header types are referred as in the code"""

ttypes: dict[str, Type[DataType]] = {
    "BOO": BOOLEAN,
    "INT": INTEGER,
    "STR": STRING,
    "NU?": NULL,
}
"""Relation between how datatypes are written on-prem and how the types are referred as in the code"""

py_ttypes: dict = {
    bool: BOOLEAN,
    int: INTEGER,
    str: STRING,
    NoneType: NULL,
}
"""Relation between python datatypes and Such. types"""

py_htypes: dict = {
    dict: KEYMAP,
    list: ARRAY
}
"""Relation between python header (iterable) types and Such. types"""
