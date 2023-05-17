# 217. Contains Duplicate

Problem: Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

```
Example 1:

Input: nums = [1,2,3,1]
Output: true
```

```
Example 2:

Input: nums = [1,2,3,4]
Output: false
```

```
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

<hr>

**Ice Burning:**

- **_Given an integer array `nums`:_** means an array(list) with just only integer value will be given and as its not mentioned that
    if will be sorted or not also by looking at the example we can say array will unsorted.
- **_return `true` if any value appears at least twice in the array:_** means if there are any duplicate
    we can return `true` if not then we can return `false`

## Solution-01

- Take the `array` convert it with `set`
- Compare the length of them
- if length is equal return `false` else return `true`
    Look inside the solution_one.py

LeetCode Result:
```
Runtime: 567 ms | Beats: 34.53%
Memory: 31.8 MB | Beats: 9.94%
```
