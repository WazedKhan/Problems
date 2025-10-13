package main

// func reverseString(value string) string {
// 	rns := []rune(value)
// 	fmt.Println("Rune: ", rns)
// 	for i, j := 0, len(rns)-1; i < j; i, j = i+1, j-1 {
// 		rns[i], rns[j] = rns[j], rns[i]
// 	}

// 	return string(rns)
// }

func IsPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	return x == reverse(x)
}

func reverse(n int) int {
	result := 0
	for n > 0 {
		result = result*10 + n%10
		n = n/10
	}
	return result
}
