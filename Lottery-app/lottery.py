import random


def main():
    print "Welcome to lottery generator"
    try:
        number = int(raw_input("How many random numbers do you want? "))
        number_range = int(raw_input("In range from 1 to "))
        if number < number_range:
            print generate_random_numbers(number, number_range)
            print "Good luck!"
        else:
            print "Your range is to small"
    except ValueError:
        print "Please enter a whole number."


def generate_random_numbers(number, number_range):
    list_of_numbers = []
    while len(list_of_numbers) != number:
        x = random.randint(1, number_range)
        if x not in list_of_numbers:
            list_of_numbers.append(x)
    return list_of_numbers


if __name__ == "__main__":
    main()
