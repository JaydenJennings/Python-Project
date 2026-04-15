import random
print("Welcome to rock, paper, scissors!")
print("The game is best of 3")

player_score = 0
computer_score = 0

while player_score < 2 and computer_score < 2:

    print("Enter your choice: rock, paper, or scissors")
    choice = input().lower()

    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    print(f"computer chose: {computer_choice}")

    if choice == computer_choice:
        print("its a tie!")

    elif choice == "rock" and computer_choice == "scissors":
        print("you win!")
        player_score += 1

    elif choice == "paper" and computer_choice == "rock":
        print("you win!")
        player_score += 1

    elif choice == "scissors" and computer_choice == "paper":
        print("you win!")
        player_score += 1

    else:
        print("you lose!")
        computer_score += 1

    print("Score:", player_score, "-", computer_score)

if player_score == 2:
    print("You won best of 3!")
else:
    print("Computer won best of 3!")