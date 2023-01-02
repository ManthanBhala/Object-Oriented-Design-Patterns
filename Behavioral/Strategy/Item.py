from Strategy import DiscountStrategy

class Item:

    def __init__(self):
        self.discountStrategy = DiscountStrategy()
    
    def setDiscountStrategy(self, discountStrategy):
        self.discountStrategy = discountStrategy
    
    def getDiscount(self):
        self.discountStrategy.getDiscount()
