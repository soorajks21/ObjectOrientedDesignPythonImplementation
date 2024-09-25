# inventory.py
from Guitar import Guitar  # Import the Guitar class

class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, serial_number, price, builder, model, guitar_type, back_wood, top_wood):
        guitar = Guitar(serial_number, price, builder, model, guitar_type, back_wood, top_wood)
        self.guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in self.guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar
        return None

    def search(self, search_guitar):
        for guitar in self.guitars:
            builder = search_guitar.get_builder()
            if builder and builder != guitar.get_builder():
                continue
            model = search_guitar.get_model()
            if model and model != guitar.get_model():
                continue
            guitar_type = search_guitar.get_type()
            if guitar_type and guitar_type != guitar.get_type():
                continue
            back_wood = search_guitar.get_back_wood()
            if back_wood and back_wood != guitar.get_back_wood():
                continue
            top_wood = search_guitar.get_top_wood()
            if top_wood and top_wood != guitar.get_top_wood():
                continue
            return guitar
        return None


def main():
    inventory = Inventory()
    initialize_inventory(inventory)

    what_erin_likes = Guitar("", 0, "Fender", "Stratocastor", "Electric", "Alder", "Alder")
    guitar = inventory.search(what_erin_likes)

    if guitar:
        print(f"Erin, you might like this {guitar.get_builder()} {guitar.get_model()} "
              f"{guitar.get_type()} guitar:\n   {guitar.get_back_wood()} back and sides,\n   "
              f"{guitar.get_top_wood()} top.\nYou can have it for only ${guitar.get_price()}!")
    else:
        print("Sorry, Erin, we have nothing for you.")


def initialize_inventory(inventory):
    inventory.add_guitar("11277", 3999.95, "Collings", "CJ", "Acoustic", "Indian Rosewood", "Sitka")
    inventory.add_guitar("V95693", 1499.95, "Fender", "Stratocastor", "Electric", "Alder", "Alder")
    inventory.add_guitar("V9512", 1549.95, "Fender", "Stratocastor", "Electric", "Alder", "Alder")
    inventory.add_guitar("122784", 5495.95, "Martin", "D-18", "Acoustic", "Mahogany", "Adirondack")
    inventory.add_guitar("76531", 6295.95, "Martin", "OM-28", "Acoustic", "Brazilian Rosewood", "Adirondack")
    inventory.add_guitar("70108276", 2295.95, "Gibson", "Les Paul", "Electric", "Mahogany", "Maple")
    inventory.add_guitar("82765501", 1890.95, "Gibson", "SG '61 Reissue", "Electric", "Mahogany", "Mahogany")
    inventory.add_guitar("77023", 6275.95, "Martin", "D-28", "Acoustic", "Brazilian Rosewood", "Adirondack")
    inventory.add_guitar("1092", 12995.95, "Olson", "SJ", "Acoustic", "Indian Rosewood", "Cedar")
    inventory.add_guitar("566-62", 8999.95, "Ryan", "Cathedral", "Acoustic", "Cocobolo", "Cedar")
    inventory.add_guitar("6 29584", 2100.95, "PRS", "Dave Navarro Signature", "Electric", "Mahogany", "Maple")


if __name__ == "__main__":
    main()
