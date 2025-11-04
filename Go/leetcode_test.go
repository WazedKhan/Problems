package main

import (
	"reflect"
	"testing"
)

func TestMerge(t *testing.T) {
	tests := []struct {
		name     string
		nums1    []int
		m        int
		nums2    []int
		n        int
		expected []int
	}{
		{
			name:     "standard merge",
			nums1:    []int{1, 2, 3, 0, 0, 0},
			m:        3,
			nums2:    []int{2, 5, 6},
			n:        3,
			expected: []int{1, 2, 2, 3, 5, 6},
		},
		{
			name:     "nums2 empty",
			nums1:    []int{1},
			m:        1,
			nums2:    []int{},
			n:        0,
			expected: []int{1},
		},
		{
			name:     "nums1 empty",
			nums1:    []int{0},
			m:        0,
			nums2:    []int{1},
			n:        1,
			expected: []int{1},
		},
		{
			name:     "nums2 smaller than nums1",
			nums1:    []int{2, 0},
			m:        1,
			nums2:    []int{1},
			n:        1,
			expected: []int{1, 2},
		},
		{
			name:     "reverse sorted arrays",
			nums1:    []int{4, 5, 6, 0, 0, 0},
			m:        3,
			nums2:    []int{1, 2, 3},
			n:        3,
			expected: []int{1, 2, 3, 4, 5, 6},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name+" - Merge", func(t *testing.T) {
			nums1Copy := make([]int, len(tt.nums1))
			copy(nums1Copy, tt.nums1)

			Merge(nums1Copy, tt.m, tt.nums2, tt.n)

			if !reflect.DeepEqual(nums1Copy, tt.expected) {
				t.Errorf("Merge() = %v; want %v", nums1Copy, tt.expected)
			}
		})

		t.Run(tt.name+" - MergeOptimal", func(t *testing.T) {
			nums1Copy := make([]int, len(tt.nums1))
			copy(nums1Copy, tt.nums1)

			MergeOptimal(nums1Copy, tt.m, tt.nums2, tt.n)

			if !reflect.DeepEqual(nums1Copy, tt.expected) {
				t.Errorf("MergeOptimal() = %v; want %v", nums1Copy, tt.expected)
			}
		})
	}
}

func TestGenerate(t *testing.T) {
	tests := []struct {
		numRows int
		want    [][]int
	}{
		{1, [][]int{{1}}},
		{2, [][]int{{1}, {1, 1}}},
		{3, [][]int{{1}, {1, 1}, {1, 2, 1}}},
		{4, [][]int{{1}, {1, 1}, {1, 2, 1}, {1, 3, 3, 1}}},
		{5, [][]int{{1}, {1, 1}, {1, 2, 1}, {1, 3, 3, 1}, {1, 4, 6, 4, 1}}},
		{6, [][]int{{1}, {1, 1}, {1, 2, 1}, {1, 3, 3, 1}, {1, 4, 6, 4, 1}, {1, 5, 10, 10, 5, 1}}},
	}

	for _, tt := range tests {
		got := Generate(tt.numRows)
		if !reflect.DeepEqual(got, tt.want) {
			t.Errorf("Generate(%d) = %v; want %v", tt.numRows, got, tt.want)
		}
	}
}

func TestMaxProfit(t *testing.T) {
	tests := []struct {
		prices   []int
		expected int
	}{
		{[]int{7, 1, 5, 3, 6, 4}, 5},
		{[]int{7, 6, 4, 3, 1}, 0},
		{[]int{2, 7, 1, 5, 4}, 5},
		{[]int{3, 2, 6, 1, 4}, 4},
		{[]int{}, 0},
		{[]int{1}, 0},
		{[]int{2, 1}, 0},
		{[]int{1, 2}, 1},
	}

	for _, test := range tests {
		got := MaxProfit(test.prices)
		if got != test.expected {
			t.Errorf("maxProfit(%v) = %d; want %d", test.prices, got, test.expected)
		}
	}
}

// https://leetcode.com/problems/roman-to-integer/description/
// python Solution: LeetCode/roman_to_int.py

func Test_RomanToInt(t *testing.T) {
	tests := []struct {
		s        string
		expected int
	}{
		{"III", 3},
		{"IV", 4},
		{"IX", 9},
		{"LVIII", 58},
		{"MCMXCIV", 1994},
	}

	for _, test := range tests {
		got := RomanToInt(test.s)
		if got != test.expected {
			t.Errorf("romanToInt(%s) = %d; want %d", test.s, got, test.expected)
		}
	}
}

// https://leetcode.com/problems/valid-parentheses/
// 20. Valid Parentheses

func Test_ValidParentheses(t *testing.T) {
	tests := []struct {
		s        string
		expected bool
	}{
		{"()", true},
		{"(){}[]", true},
		{"(]", false},
		{"([])", true},
		{"([)]", false},
		{"(){}}{", false},
	}

	for _, test := range tests {
		got := IsValidParentheses(test.s)
		if got != test.expected {
			t.Errorf("for %s got %t but want %t", test.s, got, test.expected)
		}
	}

}

// 217. Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/
// Python Solution: LeetCode/ContainsDuplicate.py
func Test_ContainsDuplicate(t *testing.T) {
	tests := []struct {
		nums []int
		expected bool
	}{
		{[]int{1,2,3,1}, true},
		{[]int{1,2,3,4}, false},
		{[]int{1,1,1,3,3,4,3,2,4,2}, true},
	}

	for _, test := range tests {
		got := ContainsDuplicate(test.nums)
		if got != test.expected {
			t.Errorf("for %v got %t but want %t", test.nums, got, test.expected)
		}
	}
}
