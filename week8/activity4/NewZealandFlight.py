from Flight import Flight

class NewZealandFlight(Flight):
    def __init__(self, flight_id, flight_number, departure_location, destination_location,
                 departure_time, arrival_time, departure_location_nz_postal_code, maori_language_broadcasting):
        super().__init__(flight_id, flight_number, departure_location, destination_location,
                         departure_time, arrival_time)
        self.departure_location_nz_postal_code = departure_location_nz_postal_code
        self.maori_language_broadcasting = maori_language_broadcasting

    def show_departure_location_nz_postal_code(self):
        print(f"Departure NZ Postal Code: {self.departure_location_nz_postal_code}")

    def display_core_info(self):
        super().display_core_info()
        print(f"Maori Broadcast: {'On' if self.maori_language_broadcasting else 'Off'}")

    def if_maori_language_broadcasting(self):
        if self.maori_language_broadcasting:
            return "This flight provides Māori language announcements."
        else:
            return "Māori language announcements are not available on this flight."