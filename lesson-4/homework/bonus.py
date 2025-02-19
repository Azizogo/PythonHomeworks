import random


my_score = 0
computer_score = 0


choices = {"r": "rock", "p": "paper", "s": "scissors"}

while my_score < 5 and computer_score < 5:
    comp_choice = random.choice(["r", "p", "s"])
    my_choice = input("Enter your choice: (r for rock, p for paper, s for scissors): ").strip().lower()


    print(f"You chose: {choices[my_choice]}")
    print(f"Computer chose: {choices[comp_choice]}")
    if my_choice == comp_choice:
        print(" It's a tie!")
    if (my_choice == "r" and comp_choice == "s") or \
         (my_choice == "p" and comp_choice == "r") or \
         (my_choice == "s" and comp_choice == "p"):
        print("You win this round!")
        my_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f" Score -> You: {my_score} | Computer: {computer_score}")


if computer_score == 5:
    print("Computer won")
else:
    print("You won")
