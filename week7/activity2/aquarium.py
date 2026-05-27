

from  fish import FishFactory

# singletan pattern implementation for aquarium class
class Aquarium:
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls._instance._inventory = {}
        return cls._instance
    

    fishFactory = FishFactory()
     

    def add_fish(self, fish_type: str, quantity: int):
        fish = self.fishFactory.create_product(fish_type)
        
        if fish is None:
            print("❌ Invalid fish type. Please try again.")
            return
             
        name = fish.name
        self._inventory[name] = self._inventory.get(name, 0) + quantity
        print(f"✅ Added {quantity} {name}(s) to the aquarium.")

    
 
    def display_all_fish(self):
        print("\n===== Auckland Aquarium Current Inventory =====") 
        if not self._inventory:
            print("The aquarium is currently empty.")
        else: 
            for name, qty in self._inventory.items(): 
                temp_fish = self.fishFactory.create_product(name)
                print(f"{name} ({temp_fish.category}): {qty}")
        print("================================")