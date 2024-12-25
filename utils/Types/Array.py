from utils.Statements.Statement import Statement
from utils.Types.DataType import DataType
from utils.Statements.Definition import Definition

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
    def __init__(self, subtypes):
        self.subtypes = subtypes
        super().__init__(ARRAY, [])


    def _add_child(self, child: Statement):
        if type(child) in self.subtypes:
            self.value.append(child)
