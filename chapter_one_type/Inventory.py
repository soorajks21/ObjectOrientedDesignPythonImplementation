from typing import List
from Guitar import Guitar
from Builder import Builder
from Type import Type
from Wood import Wood

class Inventory:
    def __init__(self):
        self.guitars: List[Guitar] = []  # Initialize the list of guitars

    def add_guitar(self, serial_number: str, price: float, builder: Builder, model: str, guitar_type: Type, back_wood: Wood, top_wood: Wood):
        guitar = Guitar(serial_number, price, builder, model, guitar_type, back_wood, top_wood)
        self.guitars.append(guitar)

    def search(self, search_guitar: Guitar) -> List[Guitar]:
        matching_guitars: List[Guitar] = []  # List to hold matching guitars
        for guitar in self.guitars:
            # Ignore serial number since that's unique
            # Ignore price since that's unique
            
            if search_guitar.get_builder() != guitar.get_builder():
                continue
            
            model = search_guitar.get_model().lower()
            if model and model != guitar.get_model().lower():
                continue
            
            if search_guitar.get_type() != guitar.get_type():
                continue
            
            if search_guitar.get_back_wood() != guitar.get_back_wood():
                continue
            
            if search_guitar.get_top_wood() != guitar.get_top_wood():
                continue
            
            matching_guitars.append(guitar)

        return matching_guitars  # Return the list of matching guitars
