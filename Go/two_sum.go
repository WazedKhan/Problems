package main

func TwoSum(nums []int, target int) []int {
	seen := make(map[int]int)
	for index, value := range nums {
		required := target - value
		if idx, ok := seen[required]; ok {
			return []int{index, idx}
		}
		seen[value] = index
	}
	return nil
}
