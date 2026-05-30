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

    # 修正拼写错误，并加上 self 参数
    def domestic_or_international(self):
        pass    


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
        


class DomesticFlight(NewZealandFlight):
    def __init__(self, flight_id, flight_number, departure_location, destination_location,
                 departure_time, arrival_time, departure_location_nz_postal_code, maori_language_broadcasting,
                 destination_location_nz_postal_code):
        super().__init__(flight_id, flight_number, departure_location, destination_location,
                         departure_time, arrival_time, departure_location_nz_postal_code, maori_language_broadcasting)
        self.destination_location_nz_postal_code = destination_location_nz_postal_code

    def show_destination_location_nz_postal_code(self):
        print(f"Destination NZ Postal Code: {self.destination_location_nz_postal_code}")

    def flight(self):
        print(f"I can fly domestically!")

    # 为 DomesticFlight 实现这个方法
    def domestic_or_international(self):
        print("This is a domestic flight.")


class InternationalFlight(NewZealandFlight):
    def __init__(self, flight_id, flight_number, departure_location, destination_location,
                 departure_time, arrival_time, departure_location_nz_postal_code, maori_language_broadcasting,
                 destination_country, visa_required): 
        super().__init__(flight_id, flight_number, departure_location, destination_location,
                         departure_time, arrival_time, departure_location_nz_postal_code, maori_language_broadcasting)
        self.destination_country = destination_country
        self.visa_required = visa_required
 
    def show_visa_required(self):
        if self.visa_required:
            print("Visa is required for this destination.")
        else:
            print("No visa required for this destination.")

    def domestic_or_international(self):
        print(f"This is an international flight to {self.destination_country}.")


def main():
    print("=== Test Domestic Flight ===")
    dom_flight = DomesticFlight(
        flight_id="D001",
        flight_number="NZ501",
        departure_location="Auckland",
        destination_location="Wellington",
        departure_time="08:00",
        arrival_time="09:15",
        departure_location_nz_postal_code="1010",
        maori_language_broadcasting=True,
        destination_location_nz_postal_code="6011"
    )
    dom_flight.display_core_info()  
    dom_flight.domestic_or_international()  # 不需要传 dom_flight
    print(dom_flight.if_maori_language_broadcasting())
    print()

    print("=== Test International Flight ===")
    int_flight = InternationalFlight(
        flight_id="I001",
        flight_number="NZ102",
        departure_location="Auckland",
        destination_location="Sydney",
        departure_time="10:00",
        arrival_time="13:30",
        departure_location_nz_postal_code="1010",
        maori_language_broadcasting=False,
        destination_country="Australia",
        visa_required=True
    )
    int_flight.display_core_info() 
    int_flight.show_visa_required() 
    int_flight.domestic_or_international()  # 不需要传 int_flight
    print(int_flight.if_maori_language_broadcasting())

if __name__ == "__main__":
    main()