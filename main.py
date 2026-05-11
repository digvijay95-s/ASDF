import random

def play_game():
    low=0
    high=100
    num=random.randint(low,high)
    guesses=0
    is_rn=True

    print("Python Number Guessing Game")
    print(f"Select a number between {low} and {high}")

    while is_rn:
        guess=input("Enter your guess:")
        
        if guess.isdigit():
            guess=int(guess)
            guesses+=1

            if guess<low or guess>high:
                print("That number is out of your Range")
                print(f"Please select a number between {low} and {high}")
            elif guess>num:
                print("TOO HIGH!! try again")
            elif guess<num:
                print("TOO LOW!! try again")
            else:
                print("Correct Guess!!!")
                print(f"{guess} is the right answer")
                print(f"Guesses:{guesses}")
                is_rn=False
        else:
            print("INVALID INPUT!!")
            print("Please select a number between {low} and {high}")

if __name__ == "__main__":
    while True:
        play_game()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! Goodbye.")
            break