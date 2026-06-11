import random

user_score = 0
computer_score = 0

while True:
    print("\n----- ROCK PAPER SCISSORS -----")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("\nFinal Score")
        print("User Score:", user_score)
        print("Computer Score:", computer_score)
        print("Thanks for playing!")
        break

    options = ["Rock", "Paper", "Scissors"]

    if choice in ["1", "2", "3"]:
        user_choice = options[int(choice) - 1]
        computer_choice = random.choice(options)

        print("Your Choice:", user_choice)
        print("Computer Choice:", computer_choice)

        if user_choice == computer_choice:
            print("It's a Tie!")

        elif (
            (user_choice == "Rock" and computer_choice == "Scissors")
            or (user_choice == "Paper" and computer_choice == "Rock")
            or (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            print("You Win!")
            user_score += 1

        else:
            print("Computer Wins!")
            computer_score += 1

        print("Score -> You:", user_score, "| Computer:", computer_score)

    else:
        print("Invalid choice. Please try again.")