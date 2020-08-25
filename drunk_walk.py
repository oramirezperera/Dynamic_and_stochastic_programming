import random

class Drunk: #Base class so we can generate different implementations
    def __init__(self, name): #contructor
        self.name = name


class TraditionalDrunk(Drunk): #Drunk as a parameter means it's an amplification of drunk
    
    def __init__(self, name):
        super().__init__(name) #Here you got the reference to the superclass
    
    def walk(self): #this drunk man walks randomly through four options
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)]) # random.choice picks one value of this list randomly
        #This implementation gives you the chance to change the probabilities of any value

class FallenDrunk(Drunk):

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return random.choice([(0, 0.8), (0, -1.2), (1, 0), (-1, 0)])