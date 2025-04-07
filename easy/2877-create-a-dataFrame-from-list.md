# 2877. Create a DataFrame from List

## Problem Summary  
Given a 2D list containing student IDs and ages,  
create a DataFrame with two columns: `student_id` and `age`.  
The order of rows must be preserved.

## Solution Method  
I used `pd.DataFrame()` to convert the 2D list directly into a DataFrame, specifying column names at the same time.

## Code  
→ See `easy/2877-create-a-dataFrame-from-list.py`

## What I Learned  
- **Naming matters.** Giving the input list a clear name like `student_data` makes the code self-explanatory.  
- **Column names are key.** Choosing intuitive column names like `student_id` and `age` helps keep your DataFrame readable and easy to use later.  
- Might sound obvious, but it's good to **remember that pandas assumes your list starts with rows** — so 2D list structure needs to be consistent.

## Metadata  
- Solved on: 2025-04-07  
- Time taken: ~1 minute (lol)  
- Difficulty: Easy  
