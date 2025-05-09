import random

# New static puzzles
math_riddles = [
    ("I am a number. Double me and add 6, you get 26. What number am I?", "10"),
    ("I am an odd number. Take away one letter and I become even. What am I?", "Seven"),
    ("I am a two-digit number. My digits add up to 11, and I am a multiple of 5.", "65"),
    ("I am a number less than 20, when multiplied by 3 gives 33. What am I?", "11"),
    ("You buy 3 pens for ₹15. How much does one pen cost?", "5"),
    ("A number divided by 2 gives 18. What is the number?", "36"),
    ("I am a square number between 20 and 30. What am I?", "25"),
    ("I am a number. Triple me and add 12 to get 45. What am I?", "11"),
    ("What number increases by 12 when doubled?", "6"),
    ("I am greater than 50, smaller than 60, divisible by 9. Who am I?", "54"),

    # New ones carefully created
    ("I am a number. Subtract 4 from me and you get 20. What number am I?", "24"),
    ("I am a two-digit number. My tens digit is double my units digit. I am less than 50. What number am I?", "42"),
    ("Double me and subtract 8 to get 22. What number am I?", "15"),
    ("I am a multiple of 6 and 8, and between 40 and 50. What number am I?", "48"),
    ("I am a number. When divided by 5, the result is 7. What number am I?", "35"),
    ("I am a number whose square is 144. What number am I?", "12"),
    ("I am a number. Add 15 to me, and you get 3 times my original value. What number am I?", "7.5"),
    ("I am a prime number between 40 and 50. What am I?", "43"),
    ("I am a two-digit number. Sum of digits is 9. Difference of digits is 1. What number am I?", "54"),
    ("Multiply me by 4 and you get 100. What number am I?", "25"),

    ("I am a three-digit number. The sum of my digits is 9. I am divisible by 9. What number am I?", "108"),
    ("I am a number. Subtract 10% of me and you get 90. What number am I?", "100"),
    ("If you triple me and subtract 9, you get 12. What number am I?", "7"),
    ("I am a number greater than 70 but less than 80. I am a multiple of 8. What number am I?", "72"),
    ("I am a number. When multiplied by itself, I give 81. What number am I?", "9"),
    ("I am a number. Double me and subtract 2, you get 34. What number am I?", "18"),
    ("I am a number. Add 6 to me and divide the sum by 2 to get 10. What number am I?", "14"),
    ("I am a number. If you subtract me from 50, you get 13. What number am I?", "37"),
    ("I am a number less than 100. When divided by 4, the remainder is 1. What number am I?", "65"),
    ("I am an even number. Half of me is 22. What number am I?", "44"),
    ("I am a number. Increase me by 50% and you get 30. What number am I?", "20"),
]

missing_operator = [
    ("8 __ 2 __ 2 = 12", "+, ×"),    # 8 + (2 × 2) = 12
    ("12 __ 6 __ 2 = 1", "÷, ÷"),    # (12 ÷ 6) ÷ 2 = 1
    ("7 __ 3 __ 2 = 2", "-, +"),     # 7 - 5 = 2
    ("5 __ 5 __ 5 = 15", "+, +"),    # 5 + 5 + 5 = 15
    ("9 __ 3 __ 2 = 1.5", "÷, ÷"),     # (9 ÷ 3) ÷ 2 = 1.5, but you can adjust if needed to simple
    
    ("6 __ 2 __ 4 = 7", "÷, +"),     # (6 ÷ 2) + 4 = 3 + 4 = 7
    ("18 __ 2 __ 3 = 27", "÷, ×"),   # (18 ÷ 2) × 3 = 9 × 3 = 27
    ("20 __ 5 __ 2 = 6", "÷, +"),    # (20 ÷ 5) + 2 = 4 + 2 = 6
    ("2 __ 2 __ 2 = 8", "+, ×"),     # (2 + 2) × 2 = 8
    ("8 __ 2 __ 2 = 2", "÷, ÷"),     # (8 ÷ 2) ÷ 2 = 2

    ("6 __ 2 __ 2 = 1.5", "÷, ÷"),     # (6 ÷ 2) ÷ 2 = 1.5 (adjust numbers if needed)
    ("10 __ 8 __ 2 = 6", "-, ÷"),     
    ("8 __ 4 __ 2 = 4", "÷, ×"),     # (8 ÷ 4) × 2 = 4
    ("10 __ 5 __ 1 = 3", "÷, +"),    # (10 ÷ 5) - 1 = 1

    ("12 __ 3 __ 1 = 3", "÷, -"),    # (12 ÷ 3) - 1 = 3
    ("18 __ 2 __ 3 = 3", "÷, ÷"),    # (18 ÷ 2) ÷ 3 = 3
    ("15 __ 2 __ 5 = 25", "+, ×"),   # 15 + (2 × 5) = 15 + 10 = 25
    ("5 __ 2 __ 4 = 4.5", "-, ÷"),     # (5 - 2) ÷ 4 = 0.75
    ("8 __ 2 __ 1 = 3", "÷, -"),     # (8 ÷ 2) - 1 = 3

    ("4 __ 2 __ 3 = 10", "+, ×"),     # 4 + (2 × 3) = 10
    ("7 __ 2 __ 5 = 0", "-, -"),   # 7 - 2 - 5 = 0
    ("6 __ 3 __ 1 = 2", "÷, ÷"),     # (6 ÷ 3) ÷ 1 = 2
    ("9 __ 3 __ 1 = 5", "-, -"),   # 9 - 3 - 1 = 5
    ("5 __ 1 __ 2 = 2", "-, -"),   # 5 - 1 - 2 = 2

    ("12 __ 2 __ 4 = 1.5", "÷, ÷"),    # (12 ÷ 2) ÷ 4 = 1.5
    ("10 __ 2 __ 5 = 1", "÷, ÷"),    # (10 ÷ 2) ÷ 5 = 1
    ("15 __ 5 __ 2 = 1.5", "÷, ÷"),    # (15 ÷ 5) ÷ 2 = 1.5
    ("20 __ 2 __ 3 = 7", "÷, -"),  # (20 - 2) ÷ 3 = 6

    ("24 __ 2 __ 3 = 4", "÷, ÷"),    # (24 ÷ 2) ÷ 3 = 4
    ("8 __ 2 __ 3 = 1.33", "÷, ÷"),     # (8 ÷ 2) ÷ 3 = 1.333
    ("6 __ 2 __ 3 = 12", "+, ×"),     # 6 + (2 × 3) = 12
    ("14 __ 2 __ 4 = 20", "+, +"),  # (14 - 2) ÷ 4 = 3
]

math_analogies = [
    ("2 : 6 :: 3 : ?", "9"),    # ×3
    ("5 : 15 :: 7 : ?", "21"),  # ×3
    ("4 : 8 :: 6 : ?", "12"),   # ×2
    ("3 : 6 :: 5 : ?", "10"),   # ×2
    ("8 : 16 :: 6 : ?", "12"),  # ×2
    ("2 : 8 :: 3 : ?", "12"),   # ×4
    ("5 : 10 :: 9 : ?", "18"),  # ×2
    ("4 : 10 :: 6 : ?", "14"),  # +6
    ("3 : 7 :: 5 : ?", "9"),    # +4
    ("8 : 11 :: 6 : ?", "9"),   # +3
    ("7 : 21 :: 5 : ?", "15"),  # ×3
    ("6 : 18 :: 4 : ?", "12"),  # ×3
    ("9 : 27 :: 6 : ?", "18"),  # ×3
    ("2 : 5 :: 3 : ?", "6"),    # +3
    ("1 : 3 :: 2 : ?", "5"),    # +2
    ("4 : 14 :: 5 : ?", "17"),  # ×3 + 2
    ("3 : 12 :: 6 : ?", "24"),  # ×4
    ("7 : 28 :: 5 : ?", "20"),  # ×4
    ("6 : 9 :: 8 : ?", "11"),   # +3
    ("5 : 2 :: 3 : ?", "0"),    # -3
    ("9 : 12 :: 11 : ?", "14"), # +3
    ("2 : 3 :: 4 : ?", "5"),    # +1
    ("8 : 6 :: 4 : ?", "2"),    # -2
    ("5 : 9 :: 7 : ?", "13"),   # +4
    ("6 : 15 :: 8 : ?", "21"),  # ×2 +3
    ("3 : 1 :: 6 : ?", "4"),    # +1
    ("5 : 1 :: 6 : ?", "2"),    # +1
    ("7 : 4 :: 9 : ?", "6"),    # -3
    ("10 : 5 :: 6 : ?", "3"),   # ÷2
    ("12 : 6 :: 8 : ?", "4"),   # ÷2
]

number_sequences = [
    ("2, 4, 6, 8, 10, ?", "12"),     # +2
    ("3, 6, 9, 12, 15, ?", "18"),    # +3
    ("1, 2, 4, 8, 16, ?", "32"),     # ×2
    ("2, 5, 10, 17, 26, ?", "37"),   # +3, +5, +7, +9,...
    ("5, 15, 45, 135, ?", "405"),    # ×3
    ("2, 4, 8, 16, 32, ?", "64"),    # ×2
    ("1, 1, 2, 3, 5, 8, ?", "13"),   # Fibonacci
    ("6, 12, 24, 48, ?", "96"),      # ×2
    ("10, 20, 40, 80, ?", "160"),    # ×2
    ("3, 6, 12, 24, ?", "48"),       # ×2
    ("7, 14, 21, 28, ?", "35"),      # +7
    ("11, 22, 44, 88, ?", "176"),    # ×2
    ("9, 18, 27, 36, ?", "45"),      # +9
    ("4, 8, 12, 16, ?", "20"),       # +4
    ("5, 7, 11, 17, 25, ?", "35"),   # +2,+4,+6,+8
    ("2, 3, 5, 7, 11, ?", "13"),     # primes
    ("1, 3, 7, 15, 31, ?", "63"),    # ×2 +1
    ("2, 6, 14, 30, 62, ?", "126"),  # ×2+2, ×2+2...
    ("5, 6, 11, 17, 28, ?", "45"),   # +1, +5, +6, +11, +17
    ("1, 5, 14, 30, 55, ?", "91"),   # Quadratic
    ("0, 1, 1, 2, 3, 5, ?", "8"),    # Fibonacci
    ("4, 7, 10, 13, 16, ?", "19"),   # +3
    ("5, 9, 17, 33, ?", "65"),       # ×2-1
    ("6, 11, 21, 41, ?", "81"),      # ×2-1
    ("2, 5, 10, 17, ?", "26"),       # +3,+5,+7,+9
    ("3, 7, 13, 21, ?", "31"),       # +4, +6, +8
    ("10, 30, 90, 270, ?", "810"),   # ×3
    ("8, 16, 24, 32, 40, ?", "48"),  # +8
    ("7, 14, 28, 56, ?", "112"),     # ×2
    ("1, 2, 6, 24, 120, ?", "720"),  # factorial n!
]

def get_math_puzzles(puzzle_type):
    puzzles = []

    if puzzle_type == "math_riddles":
        for q, a in math_riddles:
            puzzles.append({"question": q, "answer": a})

    elif puzzle_type == "missing_operator":
        for q, a in missing_operator:
            puzzles.append({"question": q, "answer": a})

    elif puzzle_type == "math_analogies":
        for q, a in math_analogies:
            puzzles.append({"question": q, "answer": a})

    elif puzzle_type == "number_sequences":
        for q, a in number_sequences:
            puzzles.append({"question": q, "answer": a})

    return puzzles
