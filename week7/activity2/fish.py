from abc import ABC, abstractmethod
from unicodedata import name

class Factory(ABC):
    @abstractmethod
    def create_product(self, kind=None):
        pass
 
class Fish:
    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category

class GoldFish(Fish):
    def __init__(self):
        super().__init__("Goldfish", "Cold Freshwater")

class Shark(Fish):
    def __init__(self):
        super().__init__("Shark", "Marine Apex Predator")
class Angelfish(Fish):
    def __init__(self):
        super().__init__("Angelfish", "Tropical Freshwater")

class Tuna(Fish):
    def __init__(self):
        super().__init__("Tuna", "Pelagic Ocean Fish")

class Salmon(Fish):
    def __init__(self):
        super().__init__("Salmon", "Cold water migratory Fish"   )



class FishFactory(Factory):
    def create_product(self, kind: str = None) -> Fish:
        target = kind.strip().lower()
        
        if target == "goldfish": return GoldFish()
        elif target == "shark":   return Shark()
        elif target == "angelfish": return Angelfish()
        elif target == "tuna": return Tuna()
        elif target == "salmon": return Salmon()

        return None