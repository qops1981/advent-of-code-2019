#! /usr/bin/env python3

def load_module_mass_index(filename):
    file = open(filename, 'r').readlines()                  # Read the File Lines
    return [int(line.rstrip('\n')) for line in file]        # List of Lines without newline and as INT

def calculate_fuel_for_mass(mass):
    calculation = ( ( mass / 3 ) - 2 )
    if calculation <= 0:    # Setup up for recursive fuel calculation
        return 0            # Less than Zero is Zero
    else:                   # Cumulative Calculation for Fuel
        return int(calculation + calculate_fuel_for_mass(calculation))    # Fuel Calculation Per the Challenge

def main():

    module_mass_input_source = 'module_mass_input_source.txt'

    module_masses = load_module_mass_index(module_mass_input_source)

    fuel_calculation = 0

    for mass in module_masses:
        fuel_calculation += calculate_fuel_for_mass(mass)

    print("Fuel Required for Launch is :", fuel_calculation)

if __name__ == "__main__":
    main()