#! /usr/bin/env python3

from lib.int_computer_p2 import IntComputer

def load_test_diagnostic_program(filename):
    file = open(filename, 'r').read().strip("\n").split(",")      # Read the File
    return [int(line) for line in file]                           # List of INT's

def main():

    test_diagnostic_program = '../../input/day_05/TEST_input.txt'

    int_stream = load_test_diagnostic_program(test_diagnostic_program)

    IntComputer(int_stream).compute()

if __name__ == "__main__":
    main()