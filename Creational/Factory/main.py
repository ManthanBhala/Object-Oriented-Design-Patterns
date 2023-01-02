from Factory import TravelClassFactory

travelClassFactory = TravelClassFactory()
travelClass = travelClassFactory.createBooking("flight")
travelClass.bookTicket()