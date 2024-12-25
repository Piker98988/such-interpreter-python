
class DataType(object):
    """Base class for any type in such."""
    def __init__(self, reference, value):
        self.reference = reference
        """How the type is referred as in the such. code."""
        self.value = value
        """The value of the instance of any type"""

    def _tryToParseValue(self, value):
        raise NotImplementedError()

    def __str__(self):
        return f"{self.__repr__()}({self.value})"

    @classmethod
    def __repr__(cls) -> str:
        return f"{cls.__name__}"
