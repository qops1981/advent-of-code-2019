#! /usr/bin/env python3

#! /usr/bin/env python3

def load_wire_paths(filename):
    file = open(filename, 'r').read().strip("\n").split(",")      # Read the File
    return [int(line) for line in file]                           # List of INT's

def main():

    wire_path_data = '../../input/day_03/wire_paths.txt'

    wire_paths  = load_wire_paths(wire_path_data)

            
    print("1202 Alarm State is:", wire_paths[0]) 

if __name__ == "__main__":
    main()