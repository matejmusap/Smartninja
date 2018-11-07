# -*- coding: utf-8 -*-
import random


def main():
    try:
        secret_number = generate_secret_numb()
        print secret_number
        guess = int(raw_input("Unesi broj između 1 i 60: "))
        while True:
            if secret_number == guess:
                print guessing_logic(guess, secret_number)
                print "Thanks for playing!"
                return False
            elif secret_number != guess:
                print guessing_logic(guess, secret_number)
                guess = int(raw_input("Ponovno unesi broj:"))
    except Exception as e:
        print "You broke the game! Please enter a whole number."

def generate_secret_numb():
    secret_numb = random.randint(1, 60)
    return int(secret_numb)

def guessing_logic(guess, secret_numb):
    if guess == secret_numb:
        message = "Good work! You guess the number!"
        hint = secret_numb
    elif guess != secret_numb:
        message = "Wrong! Try again!"
        if guess < secret_numb:
            hint = "Secret Number is higher than your guess!"
        elif guess > secret_numb:
            hint = "Secret Number is lower than your guess!"
    return message, hint

if __name__ == "__main__":
    main()
