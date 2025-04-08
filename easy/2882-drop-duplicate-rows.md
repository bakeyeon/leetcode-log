## 2882. Drop Duplicate Rows

## Problem Summary  

## Solution Method  
Thanks to pandas, we don't have to nest two while statements and go through the list from beginning to end trying to find a match. 
We can just use drop_duplicates(subset, keep, inplace) and get the work done.  
Pro tip: if you set inplace=True, your original DataFrame gets modified directly — no copies, no mercy.

## Code  
→ See `easy/2882-drop-duplicate-rows.py`

## What I Learned  
- don't use T for True in python. It'll be only working when you code in R. 

## Metadata  
- Solved on: 2025-04-08  
- Time taken: 1 min  
- Difficulty: Easy  
