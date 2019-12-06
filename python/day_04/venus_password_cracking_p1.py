#! /usr/bin/env python3

def split_int(i):   # Splits the int as a string into its seperate characters
    return [int(d) for d in str(i)]

def has_duplicate_neighbors(n):
    numbers = split_int(n)
    ## Compare each int to its following neighbor except the last one ##
    evaluations = [ value == numbers[index + 1] for index, value in enumerate(numbers) if index != (len(numbers) - 1) ]
    return any(evaluations) # If any value is True

def is_escalating(n):
    numbers = split_int(n)
    ## Compare each int to its following neighbor except the last one ##
    evaluations = [ value <= numbers[index + 1] for index, value in enumerate(numbers) if index != (len(numbers) - 1) ]
    return all(evaluations) # If all values are True

def main():

    password_range = range(240920,789857)

    passwords = []

    for p in password_range:
        if has_duplicate_neighbors(p) and is_escalating(p):
            passwords.append(p)

    print("Passwords Quantity Matching Conditins: ", len(passwords)) # Reqest was for shortest distance

if __name__ == "__main__":
    main()