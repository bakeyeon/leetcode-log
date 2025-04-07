# 2880. Select Data

## Problem Summary  
Given a DataFrame of students, select the name and age of the student with `student_id == 101`.

## Solution Method  
Used `.loc[]` to filter rows where `student_id == 101`, and selected only the `name` and `age` columns.

## Code  
→ See `easy/2880-select-data.py`

## What I Learned  
- My Java instincts kicked in and made me want to use parentheses in the return statement — but in Python, square brackets alone are fine.  
- When using `.loc`, always wrap both the row filter and the column list inside square brackets: `df.loc[condition, ['col1', 'col2']]`.  
- Also: don't forget to include the DataFrame name before calling `.loc` — `students.loc[...]`, not just `loc[...]`.

## Metadata  
- Solved on: 2025-04-07  
- Time taken: ~30 seconds  
- Difficulty: Easy  
