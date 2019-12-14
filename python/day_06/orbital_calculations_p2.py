#! /usr/bin/env python3

from lib.orbital_computer_p2 import OrbitalComputer
import pprint

def load_orbital_map(filename):
    return open(filename, 'r').read().split("\n")[:-1]  # Read the File and trim empty newline

def main():

    orbital_map = '../../input/day_06/orbital_map_input.txt'

    orbits      = [ o.split(')') for o in load_orbital_map(orbital_map) ]

    ## Test Data ##
    # orbits = [['COM','B'],['B','C'],['C','D'],['D','E'],['E','F'],['B','G'],['G','H'],['D','I'],['E','J'],['J','K'],['K','L'],['K','YOU'],['I','SAN']]

    computer = OrbitalComputer(orbits)

    print("Orbital Correct will require %d transfers" % (computer.compute_orbital_transfers('YOU','SAN')))

if __name__ == "__main__":
    main()

