from abc import ABC, abstractmethod


class Factory(ABC):

    @abstractmethod
    def create_product(self, kind = None):
        pass



class DeviceFactory(Factory):
    
    def create_product(self, kind = None, name = None):
        target = kind.strip().lower()
        if target == "light":
            return Light(name)
        elif target == "fan":
            return Fan(name)
        elif target == "air conditioner":
            return AirConditioner(name)
        elif target == "heater":
            return Heater(name)



class SmartDevice:
    def __init__(self, name, kind):
        self.name = name 

    def turn_off(self):
        self.status = "off"
 
    def turn_on(self):
        self.status = "on"
 

class Light(SmartDevice):
    def __init__(self, name):
        self.name = name
        self.status = "off"
        self.brightness = 0
        self.kind = "light"

    def turn_on(self):
        self.status = "on"
        self.brightness = 100

    def view_status(self):
        print(f"{self.name} is {self.status} with brightness {self.brightness}")

class Fan(SmartDevice):
    def __init__(self, name):
        self.name = name
        self.status = "off"
        self.kind = "fan"

class AirConditioner(SmartDevice):
    def __init__(self, name):
        self.name = name
        self.status = "off"
        self.kind = "air conditioner"

class Heater(SmartDevice):
    def __init__(self, name):
        self.name = name
        self.status = "off"
        self.kind = "heater"