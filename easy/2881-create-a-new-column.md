# 2881. Create a New Column

## Problem Summary  
Add a new column `bonus` to the DataFrame, where each value is double the corresponding `salary`.

## Solution Method  
Used assignment with square brackets to create a new column based on an existing one:  
`employees['bonus'] = employees['salary'] * 2`.

## Code  
→ See `easy/2881-create-a-new-column.py`

## What I Learned  
- Column names must be written as strings in square brackets: `'bonus'`, not `bonus`.  
- By default, newly added columns appear at the end (rightmost side) of the DataFrame.  
- Want the new column to appear on the left? Reorder the columns manually like this:  
  `df = df[['bonus', 'name', 'salary']]`  
- For more flexibility, convert columns to a list and insert the new column name at index 0:  
  ```python
  cols = df.columns.tolist()  
  cols.insert(0, 'bonus')  
  df = df[cols]


## Metadata  
- Solved on: 2025-04-07  
- Time taken: ~45 seconds  
- Difficulty: Easy  
