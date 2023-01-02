class CivilEngineer:

    def __init__(self, houseBuilder):
        self.houseBuilder = houseBuilder
    
    def constructHouse(self):
        self.houseBuilder.buildBasement()
        self.houseBuilder.buildFloor()
        self.houseBuilder.buildRoof()
