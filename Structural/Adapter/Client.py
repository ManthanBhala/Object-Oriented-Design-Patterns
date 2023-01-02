from Adapter import WeightMachineAdapter
from Adaptee import WeightMachine

weightMachine = WeightMachine(100)
weightMachineAdapter = WeightMachineAdapter(weightMachine)

print(weightMachineAdapter.getWeightKg())
