from enum import Enum

class Builder(Enum):
    FENDER = "Fender"
    MARTIN = "Martin"
    GIBSON = "Gibson"
    COLLINGS = "Collings"
    OLSON = "Olson"
    RYAN = "Ryan"
    PRS = "PRS"
    ANY = "Unspecified"

    def __str__(self):
        return self.value
