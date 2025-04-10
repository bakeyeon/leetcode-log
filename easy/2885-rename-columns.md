# 2885. Rename Columns

## Problem Summary
Given a DataFrame `students`,  
rename specific columns according to the given mapping.

## Solution Method
- Used the `DataFrame.rename()` method from pandas.
- Passed a dictionary to the `columns` parameter to rename:
  - `"id"` → `"student_id"`
  - `"first"` → `"first_name"`
  - `"last"` → `"last_name"`
  - `"age"` → `"age_in_years"`
- This is a clean and idiomatic way to rename columns in pandas.

## Code (simple version)
→ See easy/2885-rename-columns.py

```python
API Reference: DataFrame.rename(...)

DataFrame.rename(
    mapper=None,
    index=None,
    columns=None,
    axis=None,
    copy=True,
    inplace=False,
    level=None,
    errors='raise'
)
```

## Argument Definitions
- mapper, index, columns: Dictionaries used to rename index or columns. In this problem, we used columns.
- axis: Specifies whether to rename index or columns. If columns argument is provided, this is implicitly handled.
- copy: True (default): returns a new DataFrame.
        False: modifies the original.
- inplace: True: renames in-place, returns None.
           False (default): returns a new DataFrame with changes.
- level: Used for multi-level index DataFrames.
- errors: 'raise' (default): raises an error if a label doesn’t exist.
          'ignore': skips invalid keys silently.

## What I learned
- Got comfortable with the standard way to rename columns in pandas.
- Learned about the flexibility and options of rename(), such as inplace, errors, and level.

## Metadata
Solved on: 2025-04-10
Time taken: ~2 minutes
Difficulty: Easy
