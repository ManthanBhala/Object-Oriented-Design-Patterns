from Product import TravelClass

class FlightClass(TravelClass):

    def bookTicket(self):
        print("Flight Booked")

class BusClass(TravelClass):

    def bookTicket(self):
        print("Bus Booked")