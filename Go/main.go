package main

import "fmt"

func main() {
	fmt.Println("Go in problem solving")
	palindromeRes := IsPalindrome(212)
	fmt.Println("Is Palindrome (212): ", palindromeRes)
	parentheses := IsValidParentheses("(){}}{")
	fmt.Println("Is Valid Parentheses: ", parentheses)
	containsDuplicates := ContainsDuplicate([]int{1,2,3,1})
	fmt.Println("Contains Duplicates: ", containsDuplicates)
}
