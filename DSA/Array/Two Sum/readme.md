# Two Sum - 01 | LeetCode

Problem link: <https://leetcode.com/problems/two-sum/>

<p>
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


````
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
````


</p>

<hr>

## Information to take from Problem set

-   An array of integer with name `nums` will be given (let assume that there will be only integers)
-   Another integer with variable name `target`(single integer) will be given
-   `We need to return index no of two value` | when we add this two value the addition(+) value should be same as `target`
-   We are assured that there will exactly one solution to find the `target`

**So if we add two number from the array(nums) and there value is same as the value of target and then we can return the index no of that two value we added to get target**

## Pseudocode

1.