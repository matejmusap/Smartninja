# -*- coding: utf-8 -*-
import random
def main():
    try:
        secret_number = random.randint(1, 35)
        print secret_number
        guess = int(raw_input("Unesi broj između 1 i 35: "))
        while True:
            if guess == secret_number:
                print "Bravo! Pogodili ste tajni broj"
                print "Tajni broj je " + str(guess)
                break
            elif guess != secret_number:
                print "Pogrešno! pokušaj ponovno!"
                guess = int(raw_input("Ponovno unesi broj:"))
    except Exception as e:
        print "Please enter a whole number."
if __name__ == "__main__":
    main()