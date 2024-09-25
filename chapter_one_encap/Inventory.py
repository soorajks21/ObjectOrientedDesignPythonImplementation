from typing import List
from Guitar import Guitar
from GuitarSpec import GuitarSpec
from Builder import Builder
from Type import Type
from Wood import Wood

class Inventory:
    def __init__(self):
        self.guitars: List[Guitar] = []  # Initialize the list of guitars

    def add_guitar(self, serial_number: str, price: float, spec : GuitarSpec):
        guitar = Guitar(serial_number, price, spec)
        self.guitars.append(guitar)

    def search(self, search_guitar: GuitarSpec) -> List[Guitar]:
        matching_guitars: List[Guitar] = []  # List to hold matching guitars
        for guitar in self.guitars:
            # Ignore serial number since that's unique
            # Ignore price since that's unique
            guitarSpec = guitar.get_spec()
            if guitarSpec.matches(search_guitar):
            
            # if search_guitar.get_builder() != guitarSpec.get_builder():
            #     continue
            
            # model = search_guitar.get_model().lower()
            # if model and model != guitarSpec.get_model().lower():
            #     continue
            
            # if search_guitar.get_type() != guitarSpec.get_type():
            #     continue
            
            # if search_guitar.get_back_wood() != guitarSpec.get_back_wood():
            #     continue
            
            # if search_guitar.get_top_wood() != guitarSpec.get_top_wood():
            #     continue
            
                matching_guitars.append(guitar)

        return matching_guitars  # Return the list of matching guitars
