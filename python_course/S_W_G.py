import random

def snakeGame():
    choices = ["Gun","Snake","Water"]
    choose_compu = random.choose(choices)
    print(choices,choose_compu)
snakeGame()

# import random

# def snakeGame():
#     choices = ["Gun", "Snake", "Water"]
#     computer_choice = random.choice(choices)

#     choose = input("Choose your weapon: 'Gun', 'Snake', or 'Water' (or 'Quit' to exit): ").capitalize()

#     while choose not in choices + ["Quit"]:
#         print("Invalid choice, please choose among 'Gun', 'Snake', or 'Water'.")
#         choose = input("Choose your weapon: 'Gun', 'Snake', or 'Water' (or 'Quit' to exit): ").capitalize()

#     if choose == "Quit":
#         print("Thanks for playing!")
#         return
#     print(f"You chose: {choose}\nComputer chose: {computer_choice}")

#     if choose == computer_choice:
#         print("It's a tie!")
#     elif (choose == "Gun" and computer_choice == "Snake") or \
#         (choose == "Snake" and computer_choice == "Water") or \
#         (choose == "Water" and computer_choice == "Gun"):
#         print("You win!")
#     else:
#         print("You lose!")

# # Play multiple rounds
# while True:
#     snakeGame()