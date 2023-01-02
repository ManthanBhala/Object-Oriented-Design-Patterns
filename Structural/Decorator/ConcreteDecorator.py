from Decorator import PizzaDecorator

class Panner(PizzaDecorator):

    def __init__(self, pizza):
        super().__init__(pizza)

    def getPrice(self):
        return self.pizza.getPrice() + 80

class Jalepano(PizzaDecorator):

    def __init__(self, pizza):
        super().__init__(pizza)

    def getPrice(self):
        return self.pizza.getPrice() + 50

class Babycorn(PizzaDecorator):

    def __init__(self, pizza):
        super().__init__(pizza)

    def getPrice(self):
        return self.pizza.getPrice() + 30