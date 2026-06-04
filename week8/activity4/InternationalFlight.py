from NewZealandFlight import NewZealandFlight


class InternationalFlight(NewZealandFlight):
    def __init__(self, flight_id, flight_number, departure_location, destination_location,
                 departure_time, arrival_time, departure_location_nz_postal_code, maori_language_broadcasting,
                 destination_country, visa_required): 
        super().__init__(flight_id, flight_number, departure_location, destination_location,
                         departure_time, arrival_time, departure_location_nz_postal_code, maori_language_broadcasting)
        self.destination_country = destination_country
        self.visa_required = visa_required
 
    def flight(self):
        print(f"I can fly internationally!") 
        
    def show_visa_required(self):
        if self.visa_required:
            print("Visa is required for this destination.")
        else:
            print("No visa required for this destination.")

    def domestic_or_international(self):
        print(f"This is an international flight to {self.destination_country}.")