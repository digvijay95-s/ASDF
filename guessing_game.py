import random

class GuessingGame:
    def __init__(self, low: int = 0, high: int = 100):
        self.low = low
        self.high = high
        self.target_number = 0
        self.attempts = 0
        self.is_running = False

    def _generate_number(self):
        self.target_number = random.randint(self.low, self.high)
        self.attempts = 0
        self.is_running = True

    def _get_valid_input(self) -> int:
        while True:
            user_input = input(f"Enter your guess ({self.low}-{self.high}): ")
            if user_input.isdigit():
                return int(user_input)
            print("INVALID INPUT! Please enter a whole number.")

    def play(self):
        self._generate_number()
        print("\n--- Python Number Guessing Game ---")
        print(f"I'm thinking of a number between {self.low} and {self.high}.")

        while self.is_running:
            guess = self._get_valid_input()
            self.attempts += 1

            if guess < self.low or guess > self.high:
                print(f"Out of range! Stay between {self.low} and {self.high}.")
            elif guess > self.target_number:
                print("TOO HIGH!! Try again.")
            elif guess < self.target_number:
                print("TOO LOW!! Try again.")
            else:
                print(f"\nCorrect! {guess} was the number.")
                print(f"It took you {self.attempts} attempts.")
                self.is_running = False

if __name__ == "__main__":
    game = GuessingGame(0, 100)
    
    while True:
        game.play()
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! Goodbye.")
            break