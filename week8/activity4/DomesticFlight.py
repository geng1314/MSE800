from NewZealandFlight import NewZealandFlight


class DomesticFlight(NewZealandFlight):
    def __init__(self, flight_id, flight_number, departure_location, destination_location,
                 departure_time, arrival_time, departure_location_nz_postal_code, maori_language_broadcasting,
                 destination_location_nz_postal_code):
        super().__init__(flight_id, flight_number, departure_location, destination_location,
                         departure_time, arrival_time, departure_location_nz_postal_code, maori_language_broadcasting)
        self.destination_location_nz_postal_code = destination_location_nz_postal_code

    def flight(self):
        print(f"I can fly domestically!") 

    def show_destination_location_nz_postal_code(self):
        print(f"Destination NZ Postal Code: {self.destination_location_nz_postal_code}")

    def domestic_or_international(self):
        print("This is a domestic flight.")