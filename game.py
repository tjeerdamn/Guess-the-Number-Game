import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("=" * 40)
    print("   Welcome to the Guess the Number Game!")
    print("=" * 40)
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")
    print("-" * 40)

    while not guessed_correctly:
        try:
            guess_str = input("Enter your guess (a number): ")
            guess = int(guess_str)
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            elif guess < number_to_guess:
                print("Your guess is too LOW. Try again!")
            elif guess > number_to_guess:
                print("Your guess is too HIGH. Try again!")
            else:
                guessed_correctly = True
                print("-" * 40)
                print(f"🎉 Congratulations! You guessed the number, which was {number_to_guess}.")
                print(f"You took {attempts} attempts.")
                print("=" * 40)

        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    ask_to_play_again()

def ask_to_play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower().strip()
        if choice == 'yes':
            print("\nStarting a new game...\n")
            play_game()
            break
        elif choice == 'no':
            print("Thank you for playing! See you next time. 👋")
            break
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    play_game()