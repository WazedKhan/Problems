package main

func TwoSum(nums []int, target int) []int {
	visited_values := make(map[int]int)

	for index, value := range nums {
		required_value := target - value

		if required_value_index, exists := visited_values[required_value]; exists{
			return []int{index, required_value_index}
		}
		// required value not in visited value then insert it
		visited_values[value] = index
	}
	return nil
}