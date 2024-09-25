from Builder import Builder
from Type import Type
from Wood import Wood
from GuitarSpec import GuitarSpec

class Guitar:
    def __init__(self, serial_number: str, price: float, spec : GuitarSpec):
        self.serial_number = serial_number  # Type: str
        self.price = price                    # Type: float
        self.spec = spec

    def get_serial_number(self) -> str:
        return self.serial_number

    def get_price(self) -> float:
        return self.price

    def set_price(self, new_price: float):
        self.price = new_price

    def get_spec(self):
        return self.spec

   

# Example usage
guitar = Guitar("SN12345", 1500.00, GuitarSpec("Gibson", "Les Paul", "Electric", "Mahogany", "Maple", 12))

# Accessing and modifying attributes using the getter and setter methods
print(guitar.get_serial_number())  # Output: SN12345
print(guitar.get_price())  # Output: 1500.00
guitar.set_price(1600.00)
print(guitar.get_price())  # Output: 1600.00
