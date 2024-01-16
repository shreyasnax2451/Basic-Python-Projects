import random

def guess_number_by_computer():
    guess = None
    lower_limit = 0
    upper_limit = 10 # guess between 0 and 10
    while not guess:
        guess_by_cp = random.randint(lower_limit, upper_limit)
        input_statement = "{} is higher, lower than correct answer or correct answer".format(guess_by_cp)
        result = input(input_statement)
        if result == 'h':
            upper_limit = guess_by_cp
        elif result == 'l':
            lower_limit = guess_by_cp
        else:
            print('Yay! Computer Guessed it Right!')
            break


guess_number_by_computer()