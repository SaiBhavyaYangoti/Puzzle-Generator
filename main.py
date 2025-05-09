from puzzles.math_puzzles import (
    generate_arithmetic_sequence,
    generate_square_number_puzzle
)
from puzzles.english_puzzles import get_english_puzzles
from datetime import datetime

def generate_and_save_puzzles():
    puzzles = []

    # Generate multiple math puzzles
    math_generators = [
        generate_arithmetic_sequence,
        generate_square_number_puzzle
    ]

    for func in math_generators:
        q, a, e = func()
        puzzles.append(("Math", q, a, e))

    # Add all predefined English puzzles
    for q, a in get_english_puzzles():
        puzzles.append(("English", q, a, ""))  # No explanation needed for these

    # Format and save
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"puzzles_{today}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        idx = 1
        for subject, q, a, e in puzzles:
            f.write(f"{idx}. [{subject}] {q}\n")
            f.write(f"   Answer: {a}\n")
            if e:
                f.write(f"   Explanation: {e}\n")
            f.write("\n")
            idx += 1

    print(f"Puzzles saved to {filename}")

if __name__ == "__main__":
    generate_and_save_puzzles()
