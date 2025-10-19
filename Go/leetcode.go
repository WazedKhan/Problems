package main

import (
	"math"
	"sort"
	"strconv"
)

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

	for left <= right{
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


func CountSymmetricIntegers(low int, high int) int {
	symmetric_count := 0

	for i := low; i <= high; i++ {
		if is_symmetric(i) {
			symmetric_count ++
		}
	}
	return symmetric_count
}

func is_symmetric(num int) bool{
	s := strconv.Itoa(num)
	
	if len(s) % 2 != 0{
		return false
	}
	left_sum := 0
	right_sum := 0

	for i := 0; i < len(s) / 2; i++{
		left_sum += int(s[i] - '0')
		right_sum += int(s[len(s) - 1 - i] - '0')
	}

	return left_sum == right_sum
}

// https://leetcode.com/problems/plus-one/?envType=problem-list-v2&envId=array
// python Solution: LeetCode/easy/plus_one_066.py

func PlusOne(digits []int) []int {
	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i] < 9 {
			digits[i]++
			return digits
		}
		digits[i] = 0
	}
	return append([]int{1}, digits...)
}

// # https://leetcode.com/problems/merge-sorted-array/?envType=problem-list-v2&envId=array
// python Solution: LeetCode/easy/merge_sorted_array_88.py

func Merge(nums1 []int, m int, nums2 []int, n int)  {
    for i :=0; i < n; i++{
		nums1[m+i] = nums2[i]
	}
	sort.Ints(nums1)
}


func MergeOptimal(nums1 []int, m int, nums2 []int, n int) {
	i := m -1
	j := n - 1
	k := m + n -1

	for i >= 0 && j >=0 {
		if nums1[i] > nums2[j] {
			nums1[k] = nums1[i]
			i --
		}else{
			nums1[k] = nums2[j]
			j --
		}
		k --
	}

	for j >= 0 {
		nums1[k] = nums2[j]
		j --
		k --
	}
}

func Generate(numRows int) [][]int{
	triangle := [][]int{{1}}

	for i := 1; i < numRows; i++ {
		prev_rows := triangle[i - 1]
		row := []int{1}

		for j := 1; j < i; j ++ {
			row = append(row, (prev_rows[j - 1] + prev_rows[j]))
		}

		row = append(row, 1)
		triangle = append(triangle, row)
	}
	return triangle
}

func MaxProfit(prices []int) int {
    min_price := math.MaxInt
	best_profit := 0

	for _, value := range prices{
		if min_price > value{
			min_price = value
		}

		if value - min_price > best_profit{
			best_profit = value - min_price
		}
	}
	return best_profit
}

// https://leetcode.com/problems/roman-to-integer/description/
// python Solution: LeetCode/roman_to_int.py
// 13. Roman to Integer

func RomanToInt(s string) int {
	romToIntMap := map[string]int {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
	var previousRom, currentRom int
	result := 0
	for i := len(s) - 1; i >= 0; i-- {
		currentRom = romToIntMap[string(s[i])]
		if currentRom < previousRom {
			result -= currentRom
		} else {
			result += currentRom
		}
		previousRom = currentRom
	}
	return result
}