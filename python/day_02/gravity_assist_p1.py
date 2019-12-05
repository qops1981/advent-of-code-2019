#! /usr/bin/env python3

def load_gravity_assist_program(filename):
    file = open(filename, 'r').read().strip("\n").split(",")      # Read the File
    return [int(line) for line in file]                           # List of INT's

def main():

    gravity_assist_program = '../../input/day_02/gravity_assist_input.txt'

    int_stream = load_gravity_assist_program(gravity_assist_program)

    int_stream[1] = 12   # Per Challenge this value is set
    int_stream[2] = 2    # Per Challenge this value is set

    for i, compute_value in enumerate(int_stream):
        if i % 4 == 0:      # Shifting by 4 for Operator Value

            if compute_value == 99: # The 99 Operator Value signals HAULT
                break

            action, value_one_pos, value_two_pos, store_pos, *_ = int_stream[i:-1]   # Set Required Positions

            if  compute_value == 1:     # Operator 1 is addition of the provided positions
                int_stream[store_pos] = (int_stream[value_one_pos] + int_stream[value_two_pos])
            elif compute_value == 2:    # Operator 1 is multiplication of the provided positions
                int_stream[store_pos] = (int_stream[value_one_pos] * int_stream[value_two_pos])
            else:                       # Values other than [99, 1, 2] are invalid
                print("Unknown Operator Value:", compute_value)
                break

            
    print("1202 Alarm State is:", int_stream[0]) 

if __name__ == "__main__":
    main()