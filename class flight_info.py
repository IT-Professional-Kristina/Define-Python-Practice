class flight_info:
    def __init__ (self, name, flight_number, status, destination, gate):
     self.name = name
     self.flight_number = flight_number
     self.status = status
     self.destination = destination
     self.gate = gate

    def land(self, flight_number):
        print(f"{self.name} {self.flight_number} has landed.")
    def depart(self, destination):
        print(f"{self.name} has departed and is enroute to {self.destination}.")
    def delay(self, status, gate):
        print(f"{self.name} is {self.status} on the Terminal at gate {self.gate}.")

airplane_1 = flight_info("Delta Air Lines", "DA123", "Landed", "San Diego", "D4")
airplane_2 = flight_info("American Airlines", "A3456", "Departed", "Minnesota", "A10")
airplane_3 = flight_info("United Airlines", "U8701", "Delayed", "Ohio", "D8") 
airplane_4 = flight_info("Air France", "A128987", "Delayed", "Portugal", "B1")
airplane_5 = flight_info("British Airways", "Y23489875", "Landed", "Switzerland", "MJK23")
    
airplane_1.land("DA123")
airplane_2.depart("Minnesota")
airplane_3.delay("Delayed", "D8")
airplane_4.delay("Delayed", "B1")
airplane_5.depart("Switzerland")
