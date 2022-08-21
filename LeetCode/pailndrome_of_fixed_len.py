def kthPalindrome(queries = [1,2,3,4,5,90], intLength = 3):
    starting_point = int('1'+('0'*(intLength-1)))
    listPalindrome = []
    Output = []
    count = 0
    while len(listPalindrome) <= queries[-1]:
        val = str(count+starting_point)
        if int(val[::-1]) == count+starting_point:
            listPalindrome.append(count+starting_point)
        count = count+1

    # print(listPalindrome)

    for i in queries:
        Output.append(listPalindrome[i-1])
    return Output

print(kthPalindrome())