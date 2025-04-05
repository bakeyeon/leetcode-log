## Problem Summary
Given an integer array `nums` and an integer `target`,  
return the indices of the two numbers such that they add up to `target`.

## Solution Method
- I initially considered a brute-force approach, but it was inefficient due to its O(n²) time complexity.
- Instead, I used a hash map to optimize the solution to O(n).
- The key idea is to check whether "target - current number" has already been seen.
- I iterate through the array, and for each number, I calculate the complement (`target - num`).  
  If the complement exists in the hash map, I return the current index and the index of the complement.  
  If not, I store the current number and its index in the hash map for future lookup.

## Code
→ See `easy/0001-two-sum.py`

## What I learned
- Got more familiar with the pattern of using hash maps for efficient lookups.
- It would be a good idea to implement the same problem again in Java for practice.

## Metadata
- Solved on: 2025-04-05
- Time taken: ~30 minutes
- Difficulty: Easy
