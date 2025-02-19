import random

while True:
    number = random.randint(1,100)
    attempts = 10
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))

        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print(f"  The number was {number}")
            break

    else:
        print(f" The correct number was {number} ")

    replay = input(" (yes/y/ok to restart): ").strip().lower()