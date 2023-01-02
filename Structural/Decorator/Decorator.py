from Component import Pizza

class PizzaDecorator(Pizza):

    def __init__(self, pizza):
        self.pizza = pizza

    def getPrice(self):
        pass