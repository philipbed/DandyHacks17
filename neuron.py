"""
File contains logic to properly train a Neuron.

Author: Philip Bedward
Author: Rachael Thormann
"""
import random
import math

class ParentNeuron:

    def __init__(self, size, alpha):
        self.weights = []
        for i in range(size):
            self.weights.append(random.random())
        self.alpha = alpha
    def __str__(self):
        return str(self.weights)

    def activate(self,value):
        return ( 1/ ( 1 + math.e**(value) ) )

    def feedForward(self, inArray):
        total = 0
        for(idx, val) in enumerate( inArray ):
            total += ( val * self.weights[idx] )

        return self.activate(total)

    def train(self, inArray, desired):
        output = self.feedForward( inArray )
        error = desired - output

        for i in range(len(self.weights)):
            self.weights[i] += (self.alpha * error * inArray[i] )