package main

import (
	"reflect"
	"testing"
)

func TestTwoSum(t *testing.T) {
	tests := []struct {
		nums     []int
		target   int
		expected []int
	}{
		{nums: []int{2, 7, 11, 15}, target: 9, expected: []int{1, 0}},
		{nums: []int{3, 2, 4}, target: 6, expected: []int{2, 1}},
		{nums: []int{3, 3}, target: 6, expected: []int{1, 0}},
		{nums: []int{1, 2, 3, 4, 5}, target: 8, expected: []int{4, 2}},
		{nums: []int{1, 5, 1, 5}, target: 10, expected: []int{3, 1}},
		{nums: []int{1, 2, 3}, target: 7, expected: nil}, // No solution
	}

	for _, test := range tests {
		result := TwoSum(test.nums, test.target)
		if !reflect.DeepEqual(result, test.expected) {
			t.Errorf("For nums=%v and target=%d, expected %v but got %v", test.nums, test.target, test.expected, result)
		}
	}
}