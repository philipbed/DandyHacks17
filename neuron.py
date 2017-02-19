"""
File contains logic to properly train a Neuron.

Author: Philip Bedward
Author: Rachael Thormann
"""
import random

class ParentNeuron:

    def __init__(self, size):
        self.weights = []
        for i in range(size):
            self.weights.append(random.random())

    def __str__(self):
        return str(self.weights)

    def activate(self):
        pass

    def feedForward(self, inArray):
        total = 0

        for(idx, val) in enumerate( inArray ):
            total += (val * self.weights[idx] )

        return self.activate(total)


    def train(self):
        pass