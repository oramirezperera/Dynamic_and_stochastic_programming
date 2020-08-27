import random


def throw_dice(number_of_throws):
    throw_sequence = []

    for _ in range(number_of_throws):
        throw = random.choice([1, 2, 3, 4, 5, 6]) #it could be randint(1,7) too 
        throw_sequence.append(throw)

    return throw_sequence


def main(number_of_throws, number_of_tries):
    throws = []

    for _ in range(number_of_tries):
        throw_sequence = throw_dice(number_of_throws)
        throws.append(throw_sequence)


if __name__ == '__main__':
    number_of_throws = int(input('How many dice throws do you want? '))
    number_of_tries = int(input('How many tries do you want? '))

    main(number_of_throws, number_of_tries)