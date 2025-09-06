import random

secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")

attempts = 0

while True:
    guess_input = input("Enter your guess: ")
    attempts += 1

    if not guess_input.isdigit():
        print("Invalid input! Please enter a number.")
    elif int(guess_input) == secret_number:
        print(f"Congratulations! You guessed it right in {attempts} attempts.")
        break
    elif abs(secret_number - int(guess_input)) <= 5:
        if int(guess_input) > secret_number:
            print("Very close! Try a slightly lower number.")
        else:
            print("Very close! Try a slightly higher number.")
    elif abs(secret_number - int(guess_input)) <= 10:
        if int(guess_input) > secret_number:
            print("You are near! Try a lower number.")
        else:
            print("You are near! Try a higher number.")
    elif int(guess_input) > secret_number:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
