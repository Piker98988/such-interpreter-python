from DataType import DataType


class Typing(object):
    BOOLEAN = "BOO"
    STRING = "STR"
    INTEGER = "INT"
    NULL = "NU?"
    KEYMAP = "KYV"
    ARRAY = "LIS"

    @staticmethod
    def types():
        return [
            DataType.BOOLEAN,
            DataType.STRING,
            DataType.INTEGER,
            DataType.NULL,
            DataType.KEYMAP,
            DataType.ARRAY
        ]

    @staticmethod
    def header_types():
        return [
            DataType.KEYMAP,
            DataType.ARRAY
        ]
