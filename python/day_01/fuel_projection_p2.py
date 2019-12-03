#! /usr/bin/env python3

def load_module_mass_index(filename):
    file = open(filename, 'r').readlines()              # Read the File Lines
    return [int(line.rstrip('\n')) for line in file]    # List of Lines without newline and as INT

def calculate_fuel_for_mass(mass):
    fuel 
    return int(( mass / 3 ) - 2)    # Fuel Calculation Per the Challenge

def main():

    module_mass_input_source = 'module_mass_input_source.txt'

    module_masses = load_module_mass_index(module_mass_input_source)

    fuel_calculation = 0

    for mass in module_masses:
        fuel_calculation += calculate_fuel_for_mass(mass)

    print("Fuel Required for Launch is :", fuel_calculation)

if __name__ == "__main__":
    main()