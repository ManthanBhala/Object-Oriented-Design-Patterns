from Director import CivilEngineer
from ConcreteBuilder import TreeHouseBuilder

treeHuseBuilder = TreeHouseBuilder()
civilEngineer = CivilEngineer(treeHuseBuilder)
civilEngineer.constructHouse()