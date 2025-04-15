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

