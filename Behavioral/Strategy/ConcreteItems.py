from Item import Item
from ConcreteStrategy import *

class Jeans(Item):
    
    def __init__(self):
        super().__init__()
        super().setDiscountStrategy(OfferDiscountStrategy())
    
    def getDiscount(self):
        return super().getDiscount()

class Shirt(Item):
    
    def __init__(self):
        super().__init__()
        super().setDiscountStrategy(OfferDiscountStrategy())
    
    def getDiscount(self):
        return super().getDiscount()

class Belt(Item):
    
    def __init__(self):
        super().__init__()
        super().setDiscountStrategy(SaleDiscountStrategy())
    
    def getDiscount(self):
        return super().getDiscount()