from ConcreteComponent import *
from ConcreteDecorator import *

pizza = MargaritaPizza()
pizza = Panner(pizza)
pizza = Babycorn(pizza)

print(pizza.getPrice())