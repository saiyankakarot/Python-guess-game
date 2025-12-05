import random

# Set the minimum number
lowest_num = 1

# Difficulty selection
difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

if difficulty == "easy":
    highest_num = 50
elif difficulty == "hard":
    highest_num = 500
else:
    highest_num = 100

# Generate answer AFTER difficulty is chosen
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {lowest_num} and {highest_num}.")

while is_running:
    try:
        guess = int(input(f"Make a guess between {lowest_num} and {highest_num}: "))
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print(f"Your guess is out of bounds! Please guess between {lowest_num} and {highest_num}.")
            continue

        if guess < answer:
            print("Too low.")
        elif guess > answer:
            print("Too high.")
        else:
            print(f"You got it! The answer was {answer}.")
            print(f"You guessed it in {guesses} attempts.")
            is_running = False

    except ValueError:
        print("Please enter a valid number.")
