import random

def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I have picked a secret number. Can you guess it?")
    print("Choose a difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

def get_difficulty():
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == "1":
            return 10, 9  # Easy level, secret number is 9
        elif choice == "2":
            return 50, 53  # Medium level, secret number is 53
        elif choice == "3":
            return 100, 78  # Hard level, secret number is 78
        else:
            print("Invalid choice, please enter 1, 2, or 3.")

def play_game():
    welcome_message()
    max_num, secret_num = get_difficulty()
    attempts = 0
    print(f"I'm thinking of a number between 1 and {max_num}. Try to guess it.")
    
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess < secret_num:
                print("Too low, try again!")
            elif guess > secret_num:
                print("Too high, try again!")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

def main():
    play_game()
    while True:
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay == "yes":
            play_game()
        elif replay == "no":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Please respond with 'yes' or 'no'.")

if __name__ == "__main__":
    main()
