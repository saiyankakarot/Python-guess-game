import random
import time

while True:  # replay loop

    # ------------------ Difficulty ------------------
    lowest_num = 1
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

    if difficulty == "easy":
        highest_num = 50
    elif difficulty == "hard":
        highest_num = 500
    else:
        highest_num = 100

    # ------------------ Game Setup ------------------
    answer = random.randint(lowest_num, highest_num)
    guesses = 0
    max_attempts = 7
    prev_guess = None

    print("\nWelcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lowest_num} and {highest_num}.")
    print(f"You have {max_attempts} attempts.\n")

    start_time = time.time()

    # ------------------ Game Loop ------------------
    while True:
        try:
            guess = int(input(f"Make a guess ({lowest_num}-{highest_num}): "))
            guesses += 1

            # Out-of-bounds check
            if guess < lowest_num or guess > highest_num:
                print("\033[93mOut of bounds! Try again.\033[0m")
                continue

            # Warm / Cold Hint
            if prev_guess is not None:
                if abs(guess - answer) < abs(prev_guess - answer):
                    print("\033[96mWarmer!\033[0m")
                else:
                    print("\033[95mColder!\033[0m")
            prev_guess = guess

            # Check guess
            if guess < answer:
                print("\033[91mToo low!\033[0m")
            elif guess > answer:
                print("\033[91mToo high!\033[0m")
            else:
                print(f"\n\033[92mCorrect!\033[0m The answer was {answer}.")
                print(f"You guessed it in {guesses} attempts.")

                time_taken = round(time.time() - start_time, 2)
                print(f"Time taken: {time_taken} seconds")
                break

            # Max attempts reached?
            if guesses >= max_attempts:
                print("\n\033[91mYou've run out of attempts! Game Over.\033[0m")
                print(f"The correct answer was {answer}.")
                break

        except ValueError:
            print("\033[93mPlease enter a valid number.\033[0m")

    # ------------------ Replay Option ------------------
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != "y":
        print("\nThanks for playing!")
        break
