import random


def generate_random_numbers(number, range):
    list_of_numbers = []
    while len(list_of_numbers) != number:
        x = random.randint(1, range)
        if x not in list_of_numbers:
            list_of_numbers.append(x)
    return list_of_numbers

