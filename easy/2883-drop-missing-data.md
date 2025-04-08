## 2883. Drop Missing Data

## Problem Summary  
Sometimes rows are missing a *name* — and unless you're working with ghosts, that’s a problem.  
Time to drop the nameless ones and keep your DataFrame clean.

## Solution Method  
We use pandas’ `dropna()` method with the `subset` parameter to specifically target rows where the `'name'` column is `NaN`.  
Setting `inplace=True` makes sure the original DataFrame gets updated (no new copy, no drama).

## Code  
→ See easy/2883-drop-missing-data.py

## What I Learned  
- `axis=0`: drop rows with missing values  
- `axis=1`: drop columns with missing values  
- `how='all'`: drop if **all** values are `NaN`  
- `how='any'`: drop if **any** value is `NaN`  
- `thresh=n`: keep only rows/columns with at least `n` non-NA values  
- `subset=['col']`: focus on specific columns (a.k.a. “columns your advisor actually cares about”)

## Metadata  
- Solved on: 2025-04-08  
- Time taken: 3 min  
- Difficulty: Easy  
