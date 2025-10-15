package main

import "testing"

func TestIsPalindrome(t *testing.T) {
	tests := []struct {
		name  string
		given int
		want  bool
	}{
		{"single digit", 5, true},
		{"two digit", 44, true},
		{"two digit non-palindrome", 43, false},
		{"three digit palindrome", 121, true},
		{"three digit non-palindrome", 234, false},
		{"three negative digit non-palindrome", -121, false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			res := IsPalindrome(tt.given)
			if res != tt.want {
				t.Errorf("want %v but got %v for given %d", tt.want, res, tt.given)
			}
		})
	}
}

