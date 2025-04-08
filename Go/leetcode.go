package main

// URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=problem-list-v2&envId=array
// Python Solution: LeetCode/remove_duplicates.py
func RemoveDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	slow_pointer := 0
	for fast_pointer := 1; fast_pointer < len(nums); fast_pointer++ {
		if nums[fast_pointer] != nums[slow_pointer] {
			slow_pointer++
			nums[slow_pointer] = nums[fast_pointer]
		}
	}
	return slow_pointer + 1
}

// https://leetcode.com/problems/remove-element/description/?envType=problem-list-v2&envId=array
// Python Solution: LeetCode/easy/remove_element_027.py

func RemoveElements(nums []int, val int) int{
	if len(nums) == 0{
        return 0
    }

    k := 0
    for _, value := range nums{
        if value != val{
            nums[k] = value
            k ++
        }
    }
    return k
}