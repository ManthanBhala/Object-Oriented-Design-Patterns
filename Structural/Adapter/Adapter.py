class WeightMachineAdapter:

    def __init__(self, weightMachine):
        self.weightMachine = weightMachine
    
    def getWeightKg(self):
        return self.weightMachine.getWeightPound() * 0.45
