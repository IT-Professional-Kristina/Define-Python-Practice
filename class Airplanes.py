class Airplane:
# define the airplane
    def __init__(self, name, location, color):
        self.name = name
        self.location = location
        self.color = color
# define different methods
    def takeoff(self):
        print(f"{self.name} is taking off!")
    def land(self):
        print(f"{self.name} is landing!")
    def engine(self):
        print(f"{self.name} engine is shutting off!")
# update location
    def set_location(self, new_location):
        self.location = new_location
        
 

airplane_1 = Airplane("United Airlines", "Seattle", "Blue" )
airplane_2 = Airplane("American Airlines", "Denmark", "Red")

   
airplane_2.takeoff()
   
airplane_2.land()

airplane_1.engine()
    
airplane_1.set_location("Alaska")
    
print(f"{airplane_1.name} is now in {airplane_1.location}")
