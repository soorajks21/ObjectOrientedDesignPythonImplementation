from Builder import Builder
from Type import Type
from Wood import Wood

class Guitar:
    # Constructor (Equivalent to Java's constructor)
    def __init__(self, serial_number : str, price : float, builder : Builder, model : str, guitar_type : Type, back_wood : Wood, top_wood : Wood):
        self.__serial_number = serial_number  # Private attribute
        self.__price = price  # Private attribute
        self.__builder = builder  # Private attribute
        self.__model = model  # Private attribute
        self.__guitar_type = guitar_type  # Private attribute
        self.__back_wood = back_wood  # Private attribute
        self.__top_wood = top_wood  # Private attribute
    
    # Getter for serial_number (Equivalent to getSerialNumber() in Java)
    def get_serial_number(self):
        return self.__serial_number
    
    # Getter for price (Equivalent to getPrice() in Java)
    def get_price(self):
        return self.__price
    
    # Setter for price (Equivalent to setPrice() in Java)
    def set_price(self, new_price):
        self.__price = new_price
    
    # Getter for builder (Equivalent to getBuilder() in Java)
    def get_builder(self):
        return self.__builder
    
    # Getter for model (Equivalent to getModel() in Java)
    def get_model(self):
        return self.__model
    
    # Getter for type (Equivalent to getType() in Java)
    def get_type(self):
        return self.__guitar_type
    
    # Getter for back_wood (Equivalent to getBackWood() in Java)
    def get_back_wood(self):
        return self.__back_wood
    
    # Getter for top_wood (Equivalent to getTopWood() in Java)
    def get_top_wood(self):
        return self.__top_wood


# Example usage
guitar = Guitar("SN12345", 1500.00, "Gibson", "Les Paul", "Electric", "Mahogany", "Maple")

# Accessing and modifying attributes using the getter and setter methods
print(guitar.get_serial_number())  # Output: SN12345
print(guitar.get_price())  # Output: 1500.00
guitar.set_price(1600.00)
print(guitar.get_price())  # Output: 1600.00
