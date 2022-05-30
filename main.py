from FlightRadar24.api import FlightRadar24API
from random import randint
fr_api = FlightRadar24API()

#Arrays where data is written onto 
Airline = []
FlightCode = []
Origin = []
OriginCode = []
Destination = []
DestinationCode = []
OriginGate = []
OriginTerminal= []
DestinationTerminal = []
DestinationCarousel = []
Status = []

#Appending Details
flight = fr_api.get_flights(airline = "UAE")[randint(1,22)]
details = fr_api.get_flight_details(flight_id = flight.id)
flight.set_flight_details(details)
Airline.append(flight.airline_short_name)
FlightCode.append(flight.number)
Origin.append(flight.origin_airport_name)
OriginCode.append(flight.origin_airport_iata)
Destination.append(flight.destination_airport_name)
DestinationCode.append(flight.destination_airport_iata)
OriginGate.append(flight.origin_airport_gate)
OriginTerminal.append(flight.origin_airport_terminal)
DestinationTerminal.append(flight.destination_airport_terminal)
DestinationCarousel.append(flight.destination_airport_baggage)
Status.append(flight.status_text)

#Output Syntax
print(FlightCode, " - ", Airline)
print(OriginCode, " - ", Origin)
print(DestinationCode, " - ", Destination)
print("The flight gate is ", OriginGate, "at Terminal", OriginTerminal)
print("You will arrive at Terminal", DestinationTerminal, "and your baggage will be at Carousel", DestinationCarousel)
print(Status)
