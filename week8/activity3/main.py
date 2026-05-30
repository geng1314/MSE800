




class Flight:
    def __init__(self, flight_number, departure_location, destination_location, departure_time, arrival_time): 
        self.flight_number = flight_number     
        self.departure_location = departure_location  
        self.destination_location = destination_location       
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def flight(self):
        print(f"I believe I can fly !")

class DomesticFlight(Flight):
    def __init__(self, flight_number, departure_location, destination_location, departure_time, arrival_time, regional_zone):
        super().__init__(flight_number, departure_location, destination_location, departure_time, arrival_time)
        self.regional_zone = regional_zone

    def flight(self):
        print(f"I can fly domesticlly !")


if __name__ == "__main__":

    flight1 = Flight("AA123", "Auckland", "Wellington", "08:00", "11:00")
    flight1.flight()

    flight2 = DomesticFlight("DL456", "Auckland", "Christchurch", "09:00", "12:00", "SouthIsland")
    flight2.flight()