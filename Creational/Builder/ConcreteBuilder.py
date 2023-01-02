from Builder import HouseBuilder

class IglooHouseBuilder(HouseBuilder):
    
    def __init__(self):
        super().__init__()
    
    def buildBasement(self):
        self.house.setBasement("Ice")
    
    def buildFloor(self):
        self.house.setFloor("Ice")
    
    def buildRoof(self):
        self.house.setRoof("Ice")

class TreeHouseBuilder(HouseBuilder):
    
    def __init__(self):
        super().__init__()
    
    def buildBasement(self):
        self.house.setBasement("Wood")
    
    def buildFloor(self):
        self.house.setFloor("Wood")
    
    def buildRoof(self):
        self.house.setRoof("Wood")