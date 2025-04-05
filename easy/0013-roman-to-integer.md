# 0013. Roman to Integer

## Problem Summary
Convert a Roman numeral string into its integer representation.

## Solution Method
- I used a hash map to store the value of each Roman numeral.
- Initially, I considered comparing two adjacent characters and subtracting if the first one was smaller than the second. However, since this approach doesn't cover all cases reliably, I chose a more straightforward method.
- I stored the valid Roman numeral patterns (including special cases like "IV", "IX", etc.) in a dictionary and matched them sequentially.
- For each step, I first check for two-character combinations (e.g., "IV", "IX"), since they need to be processed before single characters.
- If a two-character combination is found, I add its value and move the index by 2.
- Otherwise, I add the value of the single character and move the index by 1.

## Code
→ See `easy/0013-roman-to-integer.py`

## What I learned
- How to handle string scanning with conditionals.
- The importance of checking longer substrings before shorter ones to avoid incorrect parsing.

## Metadata
- Solved on: 2025-04-05
- Time taken: ~25 minutes
- Difficulty: Easy
