# 228: Summary Ranges

You are given a sorted unique integer array `nums`.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range [a,b] in the list should be output as:

`"a->b" if a != b`
`"a" if a == b`

Example 1:

```
    Input: nums = [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: The ranges are:
    [0,2] --> "0->2"
    [4,5] --> "4->5"
    [7,7] --> "7"
```

Example 2:

```
    Input: nums = [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: The ranges are:
    [0,0] --> "0"
    [2,4] --> "2->4"
    [6,6] --> "6"
    [8,9] --> "8->9"
```

## Stone Break

- The Problem state that in an array there will be `unique` `integers`
- These `integer` are `sorted` and they have range between each integer like in example 1: 0, 1, 2 they are incrementing by one 1
- So their range is 1 (`nums` is covered by exactly one of the ranges) so we can put 0 to 2 in a range but not 2, 4 as their will be exactly one of the range. `2+1 != 4` but `2+2 == 4`
- And again 4, 5 are follows the same range and in the end only 7 remains as `5+1 != 7` so we can can put it as it is.

## Pseudocode

- `x` == 1
- if first element then stor it in a nested list
- if 2nd element `-` 1st element is `x`
- keep checking if `current_element + next_element` - `current_element` == `x`
- if `x` append in the `current_nested_list` if not `x` then create new nested list
- at the starting of `new_nested_list` append the `current_element`