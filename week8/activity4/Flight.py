class Flight:
    def __init__(self, flight_id, flight_number, departure_location, destination_location, departure_time, arrival_time):
        self.flight_id = flight_id
        self.flight_number = flight_number
        self.departure_location = departure_location
        self.destination_location = destination_location
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def flight(self):
        print(f"I believe I can fly !")

    def display_core_info(self):
        print("===== Flight Core Info =====")
        print(f"Flight ID: {self.flight_id}")
        print(f"Flight Number: {self.flight_number}")
        print(f"From: {self.departure_location} → To: {self.destination_location}")
        print(f"Departure: {self.departure_time} | Arrival: {self.arrival_time}")
 
    def domestic_or_international(self):
        pass  