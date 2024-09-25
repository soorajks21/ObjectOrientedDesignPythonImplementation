from enum import Enum

class Type(Enum):
    ACOUSTIC = "acoustic"
    ELECTRIC = "electric"
    UNSPECIFIED = "unspecified"  # In case a default is needed

    def __str__(self):
        return self.value
    