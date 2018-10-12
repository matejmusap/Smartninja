import random
print "Welcome to lottery generator"


def main():
    try:
        list_size = int(raw_input("How many random numbers do you want? "))
    except ValueError:
        print "Please enter a whole number."
    print generate_random_numbers(list_size)


def generate_random_numbers(number):
        list_of_numbers = []
        number_range = int(raw_input("In range from 1 to "))
        if number < number_range:
            while len(list_of_numbers) != number:
                x = random.randint(1, number_range)
                if x not in list_of_numbers:
                    list_of_numbers.append(x)
            return list_of_numbers
            print "Good luck!"
        else:
            print "Your range is to small"


if __name__ == "__main__":
    main()


