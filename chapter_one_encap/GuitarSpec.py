from Builder import Builder
from Type import Type
from Wood import Wood

class GuitarSpec:
    def __init__(self, builder: Builder, model: str, guitar_type: Type, back_wood: Wood, top_wood: Wood, numStrings : int):
        self.builder = builder  # Type: Builder
        self.model = model      # Type: str
        self.type = guitar_type  # Type: Type
        self.back_wood = back_wood  # Type: Wood
        self.top_wood = top_wood  # Type: Wood
        self.numStrings = numStrings

    def get_builder(self) -> Builder:
        return self.builder

    def get_model(self) -> str:
        return self.model

    def get_type(self) -> Type:
        return self.type

    def get_back_wood(self) -> Wood:
        return self.back_wood

    def get_top_wood(self) -> Wood:
        return self.top_wood

    def get_numStrings(self) -> int:
        return self.numStrings
    
    def matches(self, other_spec):
        if self.builder != other_spec.builder:
            return False
        if self.model and self.model != "" and self.model.lower() != other_spec.model.lower():
            return False
        if self.type != other_spec.type:
            return False
        if self.numStrings != other_spec.numStrings:
            return False
        if self.back_wood != other_spec.back_wood:
            return False
        if self.top_wood != other_spec.top_wood:
            return False
        return True
        