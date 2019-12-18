#! /usr/bin/env python3

from lib.amplifier_series_p1 import AmplifierSeries
from itertools import permutations

def load_amplifier_controll_software(filename):
    file = open(filename, 'r').read().strip("\n").split(",")      # Read the File
    return [int(line) for line in file]                           # List of INT's

def main():

    amplifier_controll_software = '../../input/day_07/amplifier_controller_software.txt'

    software = load_amplifier_controll_software(amplifier_controll_software)

    ## Tests ##
    #software = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    #software = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
    #software = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

    phases = list(range(0,5))
    permutated_phases = permutations(phases) 

    amplifier_returns = []  # Gather Return to find Max later

    for permutation in list(permutated_phases):
        phase_mix = list(permutation)   # Permutation is returned as a tuple ffrom Itertools
        series    = AmplifierSeries(software, list(phase_mix))  # Phase list sent as copy for later verbose print out
        series.input()

        print(phase_mix, series.output)
        amplifier_returns.append(series.output)

    print("Max thruster value:", max(amplifier_returns))    # Present max Thrust


if __name__ == "__main__":
    main()