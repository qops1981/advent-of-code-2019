#! /usr/bin/env python3

class IntComputer:
    def __init__(self, dataset, input_set = [], noun = None, verb = None):
        self.dataset    = dataset
        self.input_set  = input_set  # Replace user input for programmatic input
        self.output_set = []         # Store output for programmatic retrieval 

        if noun != None:
            self.dataset[1] = noun   # Per Day 02 Challenge this value is set
        if verb != None:
            self.dataset[2] = verb   # Per Day 02 Challenge this value is set

        self.instruction_position = 0

#
## Compute Operations ## START ##
#

    def opcode_compute_1(self, sets):   # Addition Compute Task
        self.dataset[sets[3]] = (self.parameter(1, sets) + self.parameter(2, sets))

    def opcode_compute_2(self, sets):   # Multiplication Compute Task
        self.dataset[sets[3]] = (self.parameter(1, sets) * self.parameter(2, sets))

    def opcode_compute_3(self, sets):   # Get & Set Input Compute Task
        if not self.input_set:
            self.dataset[sets[1]] = int(input('Enter ID of System to Test: '))
        else:
            self.dataset[sets[1]] = self.input_set.pop(0)   # Start retrieving inputs from the top of the list
            print(" <:", self.dataset[sets[1]])             # Verbose presentation of action

    def opcode_compute_4(self, sets):   # Get & Output Compute Task
        print(" :>", self.parameter(1, sets))
        self.output_set.append(self.parameter(1, sets)) # Add output values to list for later retrieval

    def opcode_compute_5(self, sets):   # Jump Instruction pointer if Non-Zero
        if self.parameter(1, sets) != 0:
            self.instruction_position = self.parameter(2, sets)

    def opcode_compute_6(self, sets):   # Jump Instruction pointer if Zero
        if self.parameter(1, sets) == 0:
            self.instruction_position = self.parameter(2, sets)

    def opcode_compute_7(self, sets):   # Set parameter if given p1 less than p2
        if self.parameter(1, sets) < self.parameter(2, sets):
            self.dataset[sets[3]] = 1
        else:
            self.dataset[sets[3]] = 0

    def opcode_compute_8(self, sets):   # Set parameter if given p1 equal to p2
        if self.parameter(1, sets) == self.parameter(2, sets):
            self.dataset[sets[3]] = 1
        else:
            self.dataset[sets[3]] = 0

#
## Compute Operations ## END ##
#

    def answer_for(self, p):        # Compute and Return
        self.compute()
        return self.dataset[p]      # Return the Requested Value

    def parameter(self, i, sets):   # Get Value based on Mode (0, position), (1, literal)
        return self.dataset[sets[i]] if int(sets[0][i]) == 0 else sets[i]

    def opcode_parameters(self, op):                    # Parse out Opcode Parameters Per Instruction
        params = [ digit for digit in ('%05d' % op) ]   # Zero Pad and Separate String Digits
        return params[:-2] + [''.join(params[-2:])]     # Ones & Tens Place to be Combined

    def step_instruction_lock(self, e):
        if   e == 3 or e == 4 : # Input & Output Instructions should only move the pointer by 2        
            steps = 2 
        elif e == 5 or e == 6 : # Jump Instructions should only move the pointer by 3
            steps = 3
        else: 
            steps = 4
        self.instruction_position += steps  # Move the pointer by the provided amount

    def compute_slice(self, i):
        c_slice    = list(self.dataset[i:(i + 4)])      # Get 4 count slice from the top as its own object
        c_slice[0] = self.opcode_parameters(c_slice[0]) # Convert Opcode into Op-Parameters
        c_slice[0].reverse()                            # Reverse the Op-Parameters to match param positions
        return c_slice
 
    def compute(self):
        for idx, elm in enumerate(self.dataset):

            if idx == self.instruction_position:

                if elm == 99:   # The 99 Operator Value signals HAULT
                    break

                set_slice = self.compute_slice(idx) # Get the top 4 Elements, Parse & Sort

                opcode    = int(set_slice[0][0])

                self.step_instruction_lock(opcode)  # Move the instruction pointer

                if hasattr(self, 'opcode_compute_' + str(opcode)):              # If Method Exists
                    getattr(self, 'opcode_compute_' + str(opcode))(set_slice)   # Call Internal Class Method by name
                else:
                    self.func_not_found(set_slice)  # Failure case if No matching method Exists
                    break

    def func_not_found(self, sets): # just in case we dont have the function
        print('No Computer Instruction: ' + str(int(sets[0][0])) + ' Found!')
