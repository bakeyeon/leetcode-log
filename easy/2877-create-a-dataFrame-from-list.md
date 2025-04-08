# 2877. Create a DataFrame from List

## Problem Summary  
Given a 2D list containing student IDs and their corresponding ages,  
construct a DataFrame with two columns: `student_id` and `age`.  
The original order of the rows must be retained.

## Solution Method  
I utilized `pd.DataFrame()` to directly convert the 2D list into a DataFrame,  
explicitly specifying the column names in the process.

## Code  
→ See `easy/2877-create-a-dataFrame-from-list.py`

## What I Learned  
- **Naming conventions matter.** Assigning a meaningful name like `student_data` to the input list enhances code clarity and readability.  
- **Column naming is crucial.** Descriptive column labels such as `student_id` and `age` make the DataFrame easier to interpret and work with.  
- It may seem obvious, but it's worth noting that pandas assumes the outer list represents rows — so maintaining a consistent 2D structure is essential.

## Metadata  
- Solved on: 2025-04-07  
- Time taken: ~1 minute 
- Difficulty: Easy  
