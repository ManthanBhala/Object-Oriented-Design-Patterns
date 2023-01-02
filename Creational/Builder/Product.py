class House:

    def __init__(self):
        self.basement = None
        self.floor = None
        self.roof = None
    
    def setBasement(self, basement):
        self.basement = basement
        print("Basement: ", basement)
    
    def setFloor(self, floor):
        self.floor = floor
        print("Floor: ", floor)
    
    def setRoof(self, roof):
        self.roof = roof
        print("Roof: ", roof)