import random

def guess_the_number():
    guess_number = random.randint(1,10)
    num_input = 0

    while guess_number != num_input:
        num_input = int(input('Enter The Number: '))
        if num_input < guess_number:
            print('Oh No! {} is lower than the correct answer'.format(num_input))
        else:
            print('Oh No! {} is higher than the correct answer'.format(num_input))
    else:
        print('You Guessed It Right. {} is correct'.format(guess_number))

guess_the_number()
