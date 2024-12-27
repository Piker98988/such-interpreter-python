from .DataType import DataType

class ARRAY(DataType):
    """A vectorial header, which will have vectors of Definitions as children."""
    def __init__(self, subtypes):
        self.subtypes = tuple(subtypes)
        super().__init__(ARRAY, [])
        self.value: list


    def _add_child(self, child):
        if child.datatype in self.subtypes:
            self.value.append(child)
        else:
            raise TypeError(f"Incorrect type for child: {child}, child type: {child.datatype} not in containing types of header: {self.subtypes} at header: {self.__str__()}")

    def __str__(self) -> str:
        return f"ARRAY({[v.__str__() for v in self.value if self.value is not None]})"

    @classmethod
    def __repr__(self):
        return f"VECH"
