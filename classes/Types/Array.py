from classes.Types.DataType import DataType
from classes.Statements.Definition import Definition

"""
class HeaderDataType(DataType):
    def __init__(self, reference, *args, **kwargs):
        if kwargs:
            for arg, kwarg in zip(args, kwargs):
                {}
            super().__init__(header)
"""


class ARRAY(DataType):
    """A vectorial header, which will have vectors of Definitions as children."""
    syntax = "VECH"
    def __init__(self, *args: Definition):
        if len(args) == 0:
            raise SyntaxError("Empty VECH header.")
        super().__init__(ARRAY, [arg for arg in args])
