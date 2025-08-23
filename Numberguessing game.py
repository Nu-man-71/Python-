import random

def number_guessing_game():
    """
        Number Guessing Game
    - Computer picks a random number between 1-100
    - Player has unlimited guesses
    - Game provides feedback (too high/low)
    - Tracks number of attempts
    """
    
    # It generate random numbers 
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I am thinking number between 1 and 100.")
    print("Can you guess it?\n")
    
    while True:
        try:
            # Player guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Checking the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"\n Congratulations! You guessed it!")
                print(f"The number was {secret_number}")
                print(f"It took you {attempts} attempts.")
                break
                
        except ValueError:
            print("Please enter a valid number!")

def play_again():
    """Ask player want to play it more or not """
    while True:
        choice = input("\nWould you like to play again? (y/n): ").lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

# Main game loop
if __name__ == "__main__":
    while True:
        number_guessing_game()
        if not play_again():
            print("Thanks you for playing")
            break