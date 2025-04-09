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

// https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=array
// Python Solution: LeetCode/easy/search_insert_position_035.py

func SearchInsert(nums []int, target int) int {
    if nums[0] >= target{
		return 0
	}

	for index := 0; index < len(nums)-1; index++{
		if nums[index] == target{
			return index
		}

		if nums[index] < target && nums[index+1] > target{
			return index + 1
		}

		if nums[len(nums)-1] == target{
			return len(nums) - 1
		}
	}

	return len(nums)
}

func SearchInsertBinarySearch(nums []int, target int) int {
	left, right := 0, len(nums)-1

	for left =< right{
		mid := (left + right) / 2
		if nums[mid] == target{
			return mid
		}
		if nums[mid] < target{
			left = mid + 1
		} else{
			right = mid - 1
		}
	}
	if left == len(nums){
		return len(nums)
	}
	return left
}
