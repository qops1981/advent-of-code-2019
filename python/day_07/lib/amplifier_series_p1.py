#! /usr/bin/env python3

from .int_computer_p1 import IntComputer

class AmplifierSeries:
    def __init__(self, dataset, phases = []):
        self.dataset    = dataset
        self.phases     = phases
        self.output     = 0

    def input(self):    # Recursive use of the IntComputer
        if len(self.phases) > 0:
            computer = IntComputer(list(self.dataset), [self.phases.pop(0),self.output])
            computer.compute()
            self.output = computer.output_set[-1]   # Build up value to be last largest value
            self.input()                            # Call self for next phase