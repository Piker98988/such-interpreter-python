"""Keymap type in such."""
from classes.Statements.Definition import Definition
from classes.Statements.Header import Header
from classes.Types.DataType import DataType


class KEYMAP(DataType):
    """
    def __init__(self, child: Header | tuple[Definition] = {}):
        super().__init__("KYV", child)
        if len(args) == 1 and args[0] == DataType.KEYMAP:
            self.subtypes = DataType.KEYMAP
        else:
            for arg in args:
                if arg in self.subtypes or arg == DataType.KEYMAP:
                    raise SyntaxError("Multiple declarations of the same type are not allowed: " + args)
                self.subtypes.append(arg)

        self.child = child


    from classes.Types.DataType import DataType


    class HeaderDataType(DataType):
        def __init__(self, reference, *args, **kwargs):
            if kwargs:
                for arg, kwarg in zip(args, kwargs):
                    {}
                super().__init__(header)
    """
    def __init__(self, subtypes, *args: Definition):
        child = {}
        # TODO The args will be Definitions, and we have to store this as a dict; the references being
        super().__init__(KEYMAP, child)