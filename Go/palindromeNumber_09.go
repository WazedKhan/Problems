package main

import (
	"fmt"
	"strconv"
)

func reverseString(value string) string {
	rns := []rune(value)
	fmt.Println("Rune: ", rns)
	for i, j := 0, len(rns)-1; i < j; i, j = i+1, j-1 {
		rns[i], rns[j] = rns[j], rns[i]
	}

	return string(rns)
}

func IsPalindrome(x int) bool {
	if x < 0 {
		return false
	}

	strX := strconv.Itoa(x)
	revStr := reverseString(strX)

	return strX == revStr
}
