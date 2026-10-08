# 🎯 Guess a Number Game

A simple command-line number guessing game written in Python. The computer picks a random number between 1 and 100, and you try to guess it. After each round, you can choose to play again or quit.

## Features

- Random number generated between **1 and 100** on every round
- Tells you instantly whether your guess was correct
- Shows both your guess and the actual number when you're wrong
- Menu to **continue** or **stop** after each round
- Uses Python's `match-case` statement for the menu

## Requirements

- **Python 3.10 or higher** (the `match-case` statement is not available in older versions)
- No external libraries needed — only the built-in `random` module

Check your Python version:

```bash
python --version
```

## How to Run

1. Save the code as `guess_number.py`
2. Open a terminal in the same folder
3. Run:

```bash
python guess_number.py
```

## How to Play

1. The game asks you to enter an integer between 1 and 100.
2. The computer generates a random number and compares it with your guess.
3. The result is displayed:
   - ✅ Correct → `YES, guess is correct`
   - ❌ Wrong → shows your number and the actual number
4. Choose what to do next:
   - Enter `1` → play again
   - Enter `2` → quit the game

## Sample Output

```
enter any integer between 1 & 100: 42
NO, guess is not correct
Entered number: 42
Actual number:  77
enter 1 for continue, Enter 2 for stop: 2
BYE
```

## How the Code Works

| Part | Description |
|------|-------------|
| `guess_a_number()` | Takes the user's guess, generates a random number with `random.randint(1, 100)`, compares both and prints the result |
| `while` loop | Keeps asking whether the user wants to continue or stop |
| `match choice` | Calls `guess_a_number()` on `1`, prints `BYE` and exits the loop on `2` |

## Project Structure

```
guess-a-number/
├── guess_number.py
└── README.md
```

## Possible Improvements

- Add hints such as "too high" / "too low"
- Allow multiple attempts per round
- Add input validation so non-numeric input doesn't crash the program
- Keep a score counter across rounds
- Let the player choose the number range

## Author

Made as a beginner Python practice project.

## License

Free to use and modify for learning purposes.
