#! /usr/bin/env python3

def split_int(i):   # Splits the int as a string into its seperate characters
    return [int(d) for d in str(i)]

def duplicate_eval(n):
    numbers = split_int(n)
    ## Compare each int to its following neighbor except the last one ##
    evaluations = [ value == numbers[index + 1] for index, value in enumerate(numbers) if index != (len(numbers) - 1) ]
    return evaluations

def escalation_eval(n):
    numbers = split_int(n)
    ## Compare each int to its following neighbor except the last one ##
    evaluations = [ value <= numbers[index + 1] for index, value in enumerate(numbers) if index != (len(numbers) - 1) ]
    return evaluations

def has_single_pair_dup(evaluation):    # Looking for the exsistance of any sible dup
    count = 0
    for e in evaluation:
        if e == True:
            count += 1
        elif e == False:
            if count == 1:
                break
            else:
                count = 0

    return count == 1   # Need one single True value on its own to be valid



def main():

    password_range = range(240920,789857)

    passwords = []

    for p in password_range:
        duplicate  = duplicate_eval(p)
        escalation = escalation_eval(p)
        if any(duplicate) and all(escalation):
            if has_single_pair_dup(duplicate):
                passwords.append(p)

    print("Passwords Quantity Matching Conditins: ", len(passwords)) # Reqest was for shortest distance

if __name__ == "__main__":
    main()