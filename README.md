Number Guessing Game.
A simple, robust CLI-based game where the player tries to guess a randomly generated number within a specific range. This project demonstrates fundamental Python concepts including loops, conditional logic, and user input validation.

Features
Input Validation: Handles non-integer inputs gracefully without crashing the program.
Range Detection: Alerts the player if their guess falls outside the specified boundaries (0-100).
Score Tracking: Keeps a running count of how many attempts the player takes to find the correct number.
Dynamic Feedback: Provides "TOO HIGH" or "TOO LOW" hints to guide the player.

Logic Flow
The program follows a structured logic path to ensure a smooth user experience:
1.  Initialization: Sets the range and generates a secret number using the `random` module.
2.  Input Phase: Captures user input and checks if it is a digit.
3.  Validation Phase: Checks if the number is within the defined `low` and `high` constants.
4.  Comparison Phase: Compares the guess to the secret number and provides feedback.
5.  Termination: Ends the loop and displays the total score once the correct number is found.

How to Run
1. Ensure you have [python](https://www.python.org/) installed.
2. Clone this repository:
   ```bash
   git clone [https://github.com/digvijay95-s/number-guessing-game.git]

Future Improvements
  Add a "Play Again" functionality.
  Implement a high-score system using file I/O.
  Add difficulty levels (Easy, Medium, Hard).
