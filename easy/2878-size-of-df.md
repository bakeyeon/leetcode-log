# 2878. Get the Size of a DataFrame

## Problem Summary  
Given a DataFrame, return its number of rows and columns as a list of two integers.

## Solution Method  
I used the `.shape` attribute of the DataFrame, which returns a tuple of (rows, columns).  
Wrapping it as a list gives the expected format.

## Code  
→ See `easy/2878-size-of-df.py`

## What I Learned  
Returning a list in Python is as simple as using square brackets — no constructor needed.
In practice, lists and tuples often feel interchangeable, but it's good to return the expected type.

## Metadata  
- Solved on: 2025-04-07  
- Time taken: ~30 seconds  
- Difficulty: Easy  
