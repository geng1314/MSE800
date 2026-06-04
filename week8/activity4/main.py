
from DomesticFlight import DomesticFlight
from InternationalFlight import InternationalFlight



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
    dom_flight.domestic_or_international()   
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
    int_flight.domestic_or_international()  
    print(int_flight.if_maori_language_broadcasting())

if __name__ == "__main__":
    main()