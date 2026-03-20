import random

choices = ["rock", "paper", "scissors"]
player = int(input("Rock(1), Paper(2), Scissors(3): ")) - 1 # keeping internal logic the same
computer = random.randint(0, 2)

# Display actual choice names
print(f"You chose: {choices[player]}")
print(f"Computer chose: {choices[computer]}")

result = (player - computer) % 3

if result == 0:
    print("Tie.")
elif result == 1:
    print("You win.")
elif result == 2:
    print("You lose.")    