import random

print("Welcome to Number Guessing Game")
print("-------------------------------------")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess > number:
        print("Too High! Try again.\n")
    elif guess < number:
        print("Too Low! Try again.\n")
    else:
        print("\nCorrect! You guessed the number.")
        print("Total Attempts:", attempts)
        break

print("\nYour Performance Rating:")
for i in range(attempts):
    print("*", end="")
