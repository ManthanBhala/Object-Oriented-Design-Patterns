from ConcreteProduct import *

class TravelClassFactory:

    def createBooking(self, input):
        if(input == "flight"):
            return FlightClass()
        elif(input == "bus"):
            return BusClass()
        else:
            return None