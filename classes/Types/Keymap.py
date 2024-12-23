"""Keymap type in such."""
from classes.Statements.Definition import Definition
from classes.Types.DataType import DataType


class KEYMAP(DataType):
    """
    A relational header, which will have as child any amount definitions.
    """
    syntax = "RELH"
    def __init__(self, subtypes, *args: Definition):
        child = {}
        for arg in args:
            child[arg.name] = arg.value
        self.subtypes = subtypes
        super().__init__(KEYMAP, child)