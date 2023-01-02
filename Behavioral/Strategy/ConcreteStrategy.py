from Strategy import DiscountStrategy

class SaleDiscountStrategy(DiscountStrategy):

    def getDiscount(self):
        print("DIscount: 15%")

class OfferDiscountStrategy(DiscountStrategy):

    def getDiscount(self):
        print("DIscount: 10%")