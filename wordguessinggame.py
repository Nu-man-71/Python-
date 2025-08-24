import random
import string

class GuessTheWord:
    def __init__(self):
        self.words = [
            'python', 'computer', 'selection', 'elephant', 'wordguess',
            'console', 'geforce', 'workspaces', 'internet', 'software',
            'keyboard', 'monitor', 'pancake', 'network', 'animation',
            'apple', 'hackathon', 'august', 'datastructure', 'facebook'
        ]
        self.word = ""
        self.guessed_word = []
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_wrong_guesses = 6
        
    def choose_word(self):
        """Choose a random word from the word list"""
        self.word = random.choice(self.words).upper()
        self.guessed_word = ['_'] * len(self.word)
        
    def display_hangman(self):
        """Display hangman based on wrong guesses"""
        stages = ["", "O", "O\n|", "O\n/|", "O\n/|\\", "O\n/|\\\n/", "O\n/|\\\n/ \\"]
        return stages[self.wrong_guesses]
    
    def display_game_state(self):
        """Display current game state"""
        print("\n" + "="*50)
        print(self.display_hangman())
        print(f"Word: {' '.join(self.guessed_word)}")
        print(f"Wrong guesses: {self.wrong_guesses}/{self.max_wrong_guesses}")
        if self.guessed_letters:
            print(f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")
        print("="*50)
    
    def make_guess(self, letter):
        """Process a letter guess"""
        letter = letter.upper()
        
        if letter in self.guessed_letters:
            print(f"You already guessed '{letter}'. Try a different letter!")
            return False
        
        self.guessed_letters.add(letter)
        
        if letter in self.word:
            # Update guessed_word with correct letter
            for i, char in enumerate(self.word):
                if char == letter:
                    self.guessed_word[i] = letter
            print(f"Good guess! '{letter}' is in the word.")
            return True
        else:
            self.wrong_guesses += 1
            print(f"Sorry! '{letter}' is not in the word.")
            return False
    
    def is_word_guessed(self):
        """Check if the word is completely guessed"""
        return '_' not in self.guessed_word
    
    def is_game_over(self):
        """Check if the game is over (won or lost)"""
        return self.is_word_guessed() or self.wrong_guesses >= self.max_wrong_guesses
    
    def play(self):
        """Main game loop"""
        print(" Welcome to the Word Guessing Game! ")
        print("Try to guess the word letter by letter!")
        print("You have 6 wrong guesses before the game ends.")
        
        self.choose_word()
        
        while not self.is_game_over():
            self.display_game_state()
            
            # Get user input
            guess = input("\nEnter a letter (or 'quit' to exit): ").strip()
            
            if guess.lower() == 'quit':
                print(f"Thanks for playing! The word was: {self.word}")
                break
            
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter!")
                continue
            
            self.make_guess(guess)
        
        # Game over
        self.display_game_state()
        
        if self.is_word_guessed():
            print(" Congratulations! You guessed the word!")
        else:
            print(f" Game Over! The word was: {self.word}")
        
        # Ask to play again
        play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if play_again == 'y':
            self.__init__()  # Reset the game
            self.play()
        else:
            print("Thanks for playing! Goodbye! ")

def main():
    game = GuessTheWord()
    game.play()

if __name__ == "__main__":
    main()