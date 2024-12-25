from typing import Type

from utils.Types.Array import ARRAY
from utils.Types.Boolean import BOOLEAN
from utils.Types.DataType import DataType
from utils.Types.Integer import INTEGER
from utils.Types.Keymap import KEYMAP
from utils.Types.NullType import NULL
from utils.Types.String import STRING

htypes: dict[str, Type[DataType]] = {
    "RELH": KEYMAP,
    "VECH": ARRAY,
}

ttypes: dict[str, Type[DataType]] = {
    "BOO": BOOLEAN,
    "INT": INTEGER,
    "STR": STRING,
    "NU?": NULL,
}
