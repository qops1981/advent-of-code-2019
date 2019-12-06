#! /usr/bin/env python3

from math import*

def load_wire_paths(filename):
    file = open(filename, 'r').readlines()                  # Read the File
    return [line.strip("\n").split(",") for line in file]   # List of directions

def directions_to_coordinates(directions):
    x, y = 0, 0
    coordinates = []

    def coordinate_key(x,y):                # Turn Coordinates into a string
        return "%d,%d" % (x,y)

    def mark_chart(position):               # Add Position as string in set
        coordinates.append(position)

    def vertical_move(direction):           # Make a Vertical Movement Calculation
        nonlocal y                          # Reference the Variable in the Parent Namespace
        y += 1 if direction == 'U' else -1
        mark_chart(coordinate_key(x,y))     # Sets like not sub lists, so strings it is.

    def horizontal_move(direction):         # Make a Horizontal Movement Calculation
        nonlocal x                          # Reference the Variable in the Parent Namespace
        x += 1 if direction == 'R' else -1
        mark_chart(coordinate_key(x,y))     # Sets like not sub lists, so strings it is.

    def move(i):                            # Make a Single Increment Movement in a Provided Vector
        vertical_move(i) if i == 'U' or i == 'D' else horizontal_move(i)

    for d in directions:                    # For Each Directional instruction
        for _ in range(int(d[1:])):         # Step for Each direction
            move(d[0])

    return coordinates                      # Return all of the Steps taken and their positions

def wire_intersections(list_1, list_2):     # Return Positions that exists in both paths
    return list_1 & list_2

def manhattan_distance(x,y):                # Return Manhattan Distance Calculation
    return abs(0 - x) + abs(0 - y)

def main():

    wire_path_data = '../../input/day_03/wire_paths.txt'

    wire_paths = load_wire_paths(wire_path_data)

    wire_1 = directions_to_coordinates(wire_paths[0])
    wire_2 = directions_to_coordinates(wire_paths[1])

    distances = []

    for c in list(wire_intersections(set(wire_1), set(wire_2))):  # For Each Intersection, Converted Set to List
        distances.append((wire_1.index(c) + 1) + (wire_2.index(c) + 1))     # Use List Index +1 as step count

    print("The Intersection with the Least steps:", min(distances)) # Reqest was for shortest distance

if __name__ == "__main__":
    main()