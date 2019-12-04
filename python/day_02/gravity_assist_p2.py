#! /usr/bin/env python3

def load_gravity_assist_program(filename):
    file = open(filename, 'r').read().strip("\n").split(",")      # Read the File
    return [int(line) for line in file]                           # List of INT's

def gravity_assist_calculation(dataset, noun, verb):
    dataset[1] = noun   # Per Challenge this value is set
    dataset[2] = verb   # Per Challenge this value is set

    for i, compute_value in enumerate(dataset):
        if i % 4 == 0:      # Shifting by 4 for Operator Value

            if compute_value == 99: # The 99 Operator Value signals HAULT
                break

            action, value_one_pos, value_two_pos, store_pos, *_ = dataset[i:-1]   # Set Required Positions

            if  compute_value == 1:     # Operator 1 is addition of the provided positions
                dataset[store_pos] = (dataset[value_one_pos] + dataset[value_two_pos])
            elif compute_value == 2:    # Operator 1 is multiplication of the provided positions
                dataset[store_pos] = (dataset[value_one_pos] * dataset[value_two_pos])
            else:                       # Values other than [99, 1, 2] are invalid
                #print("Unknown Operator Value:", compute_value)
                break

    return dataset[0]


def main():

    gravity_assist_program = 'gravity_assist_input.txt'

    module_masses = load_gravity_assist_program(gravity_assist_program)

    noun, verb, output = 0, 0, 0

    for n in range(100):    # Itterate through possible values
        if output != 19690720:
            noun = n
            for v in range(100):
                verb = v
                output = gravity_assist_calculation(list(module_masses), noun, verb)
                if output == 19690720:
                    break   # Keep going until we get the right values
        else:
            break   # Keep going until we get the right values
        
    print("Gravity Assist Value:", (100 * noun + verb)) 

if __name__ == "__main__":
    main()