from Inventory import Inventory
from Guitar import Guitar
from GuitarSpec import GuitarSpec
from Builder import Builder
from Type import Type
from Wood import Wood

def main():
    inventory = Inventory()
    initialize_inventory(inventory)

    # what_erin_likes = Guitar("", 0, Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER)
    what_erin_likes = GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 12)
    guitars = inventory.search(what_erin_likes)

    for guitar in guitars:
        print("guitar",guitar)
        print(f"Erin, you might like this {guitar.get_spec().builder} {guitar.get_spec().model} "
              f"{guitar.get_spec().type} guitar:\n   {guitar.get_spec().back_wood} back and sides,\n   "
              f"{guitar.get_spec().top_wood} top.\nYou can have it for only ${guitar.get_price()}!")
    else:
        print("Sorry, Erin, we have nothing for you.")


def initialize_inventory(inventory):
    inventory.add_guitar("11277", 3999.95, GuitarSpec( Builder.COLLINGS, "CJ", Type.ACOUSTIC, Wood.INDIAN_ROSEWOOD, Wood.SITKA, 12))
    inventory.add_guitar("V95693", 1499.95, GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 12))
    inventory.add_guitar("V9512", 1549.95, GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER,10))
    inventory.add_guitar("122784", 5495.95, GuitarSpec(Builder.MARTIN, "D-18", Type.ACOUSTIC, Wood.MAHOGANY, Wood.ADIRONDACK,12))
    inventory.add_guitar("76531", 6295.95, GuitarSpec(Builder.MARTIN, "OM-28", Type.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK,12))
    inventory.add_guitar("70108276", 2295.95, GuitarSpec(Builder.GIBSON, "Les Paul", Type.ELECTRIC, Wood.MAHOGANY, Wood.MAPLE,12))
    inventory.add_guitar("82765501", 1890.95, GuitarSpec(Builder.GIBSON, "SG '61 Reissue", Type.ELECTRIC, Wood.MAHOGANY, Wood.MAHOGANY,12))
    inventory.add_guitar("77023", 6275.95, GuitarSpec(Builder.MARTIN, "D-28", Type.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK,12))
    inventory.add_guitar("1092", 12995.95, GuitarSpec(Builder.OLSON, "SJ", Type.ACOUSTIC, Wood.INDIAN_ROSEWOOD, Wood.CEDAR,12))
    inventory.add_guitar("566-62", 8999.95, GuitarSpec(Builder.RYAN, "Cathedral", Type.ACOUSTIC, Wood.COCOBOLO, Wood.CEDAR,12))
    inventory.add_guitar("6 29584", 2100.95, GuitarSpec(Builder.PRS, "Dave Navarro Signature", Type.ELECTRIC, Wood.MAHOGANY, Wood.MAPLE,12))


if __name__ == "__main__":
    main()